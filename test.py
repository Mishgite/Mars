def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/galery', methods=['GET', 'POST'])
def carousel():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('carousel'))

    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('gallery_with_download.html', images=images)