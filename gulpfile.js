var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var minifyCSS = require('gulp-minify-css');
var browserSync = require('browser-sync').create();
var exec = require('child_process').exec;

var staticPath = './static';

gulp.task('image', function () {
  return gulp
    .src(staticPath + '/img/**/*.{gif,jpg,png,svg}')
    .pipe(gulp.dest(staticPath + '/app/img'));
});

gulp.task('sass', function () {
  return gulp
    .src(staticPath + '/css/*.scss')
    .pipe(concat('app.css'))
    .pipe(sass())
    .pipe(minifyCSS())
    .pipe(gulp.dest(staticPath + '/app'))
    .pipe(
      browserSync.reload({
        stream: true,
      })
    );
});

gulp.task('javascript', function () {
  return gulp
    .src(staticPath + '/js/*.js')
    .pipe(concat('app.js'))
    .pipe(uglify())
    .pipe(gulp.dest(staticPath + '/app'))
    .pipe(
      browserSync.reload({
        stream: true,
      })
    );
});

gulp.task('runserver', function () {
  var proc = exec('python manage.py runserver');
});

gulp.task('browserSync', ['runserver'], function () {
  browserSync.init({
    notify: false,
    port: 8000,
    proxy: 'http://127.0.0.1:8000/',
  });
});

gulp.task('watch', ['browserSync', 'sass', 'javascript', 'image'], function () {
  gulp.watch('./static/css/*.scss', ['sass']);
  gulp.watch('./static/js/*.js', ['javascript']);
  gulp.watch('./apps/**/templates/**/*.html', browserSync.reload);
});
