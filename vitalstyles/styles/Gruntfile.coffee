module.exports = (grunt) ->
  # Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json')
    watch:
      less:
        tasks: 'less'
        files: ['*.less']
    less:
      development:
        files:
          "styles.css": "styles.less"
  })

  grunt.loadNpmTasks('grunt-contrib-watch')
  grunt.loadNpmTasks('grunt-contrib-less')
  grunt.registerTask('default', [
    'less'
  ])
