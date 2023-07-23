#======================================================================================================
#
# #TODO: Need to work out number of legend columns required based on 
#        width required of legend and using the wrap method to fix
#        the width of each legend entry.
#
#======================================================================================================


from matplotlib import pyplot as plt




class FormatLegend():

    def __init__(self, maxWidth="single", fontsize=10, saveloc=".") -> None:
        
        self.axes = []
        self.lines = []
        self.labels = []

        self.SMALL_SIZE = fontsize*0.8
        self.MEDIUM_SIZE = fontsize
        self.BIGGER_SIZE = fontsize*1.2

        self.defaultfont = {"family":   "Times New Roman",
                            "size":     self.MEDIUM_SIZE,
                            }

        self.figlegend = plt.figure(figsize=(3.14961, 3.14961))

        self.defaultFormatOpts = {  'xlabel':           None,
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


    def __call__(self, *figures, **kwargs) -> plt.Figure:
        
        kwargs = self._parseInput(**kwargs)
        self._assignLines(*figures, **kwargs)
        self._formatLegend(**kwargs)

        return self.figlegend

    
    def _parseInput(self, 
                    **kwargs) -> dict:

        # Parse optional arguments or assign default values
        for key, value in self.defaultFormatOpts.items():
            if key not in kwargs:
                kwargs[key] = value

        return kwargs

    def _assignLines(self, *figures, **kwargs):

        # Concatenate all axes objects together
        for fig in figures:
            self.axes += fig.get_axes()

        # Get all lines in all axes
        for axes in self.axes:
            self.lines += axes.get_lines()
        
        # Get label for each line
        for line in self.lines:
            self.labels.append(line._label)


    def _formatLegend(self, **kwargs):
            
        if kwargs['annotate']:
            
            raise NotImplementedError("Generating legends for annotated plots is not yet implemented.")

            '''
            NOTE: Below is the old code for handling annotated legends. This will need to be updated for this
                class, along with some method of dealing with multiple figure inputs where the annotate property
                is different for both.

            obj = []
            legend_map = {}
            for line, slab in zip(axes.get_lines(), shortlabel):
                obj.append( TextLegend(slab, line.get_color()) )
            for o in obj:
                legend_map[o] = TextLegendHandler()
        
            leg = figlegend.legend(obj, label, handler_map=legend_map, prop=self.legendfont, loc="center", ncol=ncol)
            leg.get_frame().set_edgecolor("black")
            figlegend.tight_layout()
            '''
        else:
            leg = self.figlegend.legend(self.lines, self.labels, prop=self.defaultfont, loc="center", ncol=4)
            
            
        leg.get_frame().set_edgecolor("black")
        for axes in self.figlegend.axes:
            axes.remove()
        self.figlegend.tight_layout()

        

