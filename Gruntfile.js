module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    concat: {
       dist: {
         src: [
           '**/*.scss',
         ],
         dest: '.compile/build.scss',
       }
     },

    sass: {                                 // Task
       dist: {     
         files: {
           'ZP_PyDash/assets/stylesheets/application.css':'.compile/build.scss'
         }
       }
    }
  });


  //Compile SASS
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-concat');


  grunt.registerTask('default', ['concat', 'sass']);
};