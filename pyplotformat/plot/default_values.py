'''
Global constant or default values for the plot subpackage are stored here.
'''

_default_colors = [ '#e31a1c', '#1f78b4', '#33a02c',
                    '#ff7f00', '#6a3d9a', '#b15928',
                    '#fb9a99', '#a6cee3', '#b2df8a', 
                    '#fdbf6f', '#cab2d6', '#ffff99'
                    ]

_MAX_LABEL_SIZE = 24


_default_format_opts = {'xlabel':           None,
                        'ylabel':           None,
                        'title':            None,
                        'show':             False,
                        'color':            None,
                        'shortlabel':       None,
                        'annotate':         False,
                        'blackline':        False,
                        'lxpad':            1.0,
                        'lypad':            1.1,
                        'uxpad':            1.0,
                        'uypad':            1.1,
                        'xylim':            None,
                        'xscale':           None,
                        'yscale':           None
                                                }

_default_polar_format_opts = _default_format_opts
_default_polar_format_opts.update({
                                    'tlabel':           None,
                                    'rlabel':           None,
                                    'axis_shape':       'full',
                                    'orient':           'CCW',
                                    'zero_location':    'E',
                                    'rlim':             None,
                                    'lrpad':            1.0,
                                    'urpad':            1.1,
                                    'rscale':           None   
                                    })
