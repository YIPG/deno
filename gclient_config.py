# Copyright 2018-2019 the Deno authors. All rights reserved. MIT license.
solutions = [
    {
        'url': 'https://chromium.googlesource.com/v8/v8.git@7.9.8',
        'name': 'v8',
        'deps_file': 'DEPS',
        'custom_deps': {
            'v8/build': None,
            'v8/third_party/catapult': None,
            'v8/third_party/colorama/src': None,
            'v8/testing/gmock': None,
            'v8/tools/swarming_client': None,
            'v8/tools/gyp': None,
            'v8/third_party/instrumented_libraries': None,
            'v8/third_party/android_tools': None,
            'v8/third_party/depot_tools': None,
            'v8/test/wasm-js': None,
            'v8/test/benchmarks/data': None,
            'v8/test/mozilla/data': None,
            'v8/third_party/icu': None,
            'v8/test/test262/data': None,
            'v8/test/test262/harness': None,
            'v8/tools/luci-go': None
        }
    },
    {
        'url':
        'https://chromium.googlesource.com/chromium/tools/depot_tools@efce0d1b7657c440c90f0f4bce614b96672b9e0b',
        'name':
        'depot_tools'
    },
    {
        'url':
        'https://github.com/cpplint/cpplint.git@a33992f68f36fcaa6d0f531a25012a4c474d3542',
        'name':
        'cpplint'
    }
]
