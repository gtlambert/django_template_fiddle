var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat');

var baseSrcDir = 'static-dev';
var baseDestDir = 'static';

gulp.task('sass', function () {
    gulp.src(baseSrcDir + '/scss/*.scss')
        .pipe(sass())
        .pipe(gulp.dest(baseSrcDir + '/css'));
});

gulp.task('copy-foundation-styles', function() {
	gulp.src(baseSrcDir + '/components/foundation/css/foundation.min.css')
		.pipe(gulp.dest(baseDestDir + '/css'));
});

gulp.task('copy-foundation-fonts', function () {
	gulp.src(baseSrcDir + '/components/foundation-icon-fonts/foundation-icons.{ttf,woff,eof,svg}')
		.pipe(gulp.dest(baseDestDir + '/css'));
});

gulp.task('watch', function() {
	gulp.watch(baseSrcDir + '/scss/*.scss', ['sass']);
	gulp.watch(baseSrcDir + '/js/app.js', ['concat-js']);
});

gulp.task('concat-js', function() {
	gulp.src([
			baseSrcDir + '/components/fastclick/lib/fastclick.js',
			baseSrcDir + '/components/jquery/dist/jquery.min.js',
			baseSrcDir + '/components/foundation/js/foundation.min.js',
			baseSrcDir + '/js/app.js'
		])
		.pipe(concat('app.built.js'))
		.pipe(gulp.dest(baseDestDir + '/js'));
});

gulp.task('default', function() {
	gulp.start('watch');
});
