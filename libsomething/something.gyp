{
  'variables': {
    'library%': 'static_library'
  },
  'target_defaults': {
    'default_configuration': 'Debug',
    'configurations': {
      'Debug': {
        'defines': [ 'DEBUG', '_DEBUG' ],
        'cflags': [ '-g', '-O0', '-Wall' ]
      },
      'Release': {
        'defines': [ 'NDEBUG' ],
        'cflags': [ '-O3', '-Wall' ]
      }
    }
  },
  'targets': [
    {
      'target_name': 'something',
      'type': 'static_library',
      'sources': [ 'something.cc' ],
      'direct_dependent_settings': {
        'include_dirs': ['.']
      }
    }
  ]
}
