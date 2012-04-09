.PHONY: clean cleanest

wisent=../wisent-0.6.1/wisent

parser.py:	basic.wi
	$(wisent) -o parser.py basic.wi

clean:
	rm *.pyc
	rm *~

cleanest:	clean
	rm parser.py

