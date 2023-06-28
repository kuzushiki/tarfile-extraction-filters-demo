import os
import shutil
import tarfile
from flask import Flask, request, render_template, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename


ALLOWED_FILTER_VALUES = ['data', 'tar', 'fully_trusted']


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 << 20  # 1MiB
app.config['UPLOAD_FOLDER'] = './uploads'


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        if 'file' not in request.files:
            return render_template('index.html', message='No file part')
        file = request.files['file']

        if file.filename == '':
            return render_template('index.html', message='No selected file')

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            if not tarfile.is_tarfile(filepath):
                os.remove(filepath)
                return render_template('index.html', message='tarfile only')

            filter_value = request.form.get('filter')
            if filter_value == 'None':
                filter_value = None
            elif filter_value not in ALLOWED_FILTER_VALUES:
                return render_template('index.html', message='Invalid filter value')

            tar = tarfile.open(filepath)
            arcname = tar.getnames()[0]

            try:
                tar.extract(arcname, path=app.config['UPLOAD_FOLDER'], filter=filter_value)
            except tarfile.FilterError as err:
                tar.close()
                os.remove(filepath)
                return render_template('index.html', message=f'{type(err).__name__}: {err}')

            tar.close()
            os.remove(filepath)
            return send_from_directory(app.config['UPLOAD_FOLDER'], arcname, mimetype='text/plain')

    return render_template('index.html', message='')


@app.route('/reset')
def clear_uploads():
    shutil.rmtree(app.config['UPLOAD_FOLDER'], ignore_errors=True)
    os.mkdir(app.config['UPLOAD_FOLDER'])

    return redirect(url_for('upload_file'))


if __name__ == "__main__":
    app.run()
