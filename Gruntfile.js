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
    },

    // Run "grunt watch" while developing to have it keep an eye out for CSS changes
    watch: {
      scripts: {
        files: ['**/*.scss'],
        tasks: ['compile_css'],
      },
    },
  });


  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-watch');


  grunt.registerTask('compile_css', ['concat', 'sass'])


  // If we dont' tell it what to do...
  grunt.registerTask('default', ['compile_css']);
};