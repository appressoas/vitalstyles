module.exports = (grunt) ->
  # Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json')

    # Run vitalstyles.
    exec:
        vitalstyles: 'vitalstyles-cli'

    # Build LESS and run vitalstyles each time our styles changes
    watch:
      less:
        files: ['less/*.less']
        tasks: [
            'less'
            'exec:vitalstyles'
        ]
      vitalstyles:
        files: ['vitalstyles.json']
        tasks: [
            'exec:vitalstyles'
        ]
    less:
      development:
        files:
          "styles.css": "less/styles.less"
  })

  grunt.loadNpmTasks('grunt-contrib-watch')
  grunt.loadNpmTasks('grunt-contrib-less')
  grunt.loadNpmTasks('grunt-exec')
  grunt.registerTask('default', [
    'less'
  ])
