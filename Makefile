FILE = main.py
RUN = echo "" && echo "" && echo "Compilação concluida. Executando..." && echo "" && python $(FILE) && echo ""
ROUTERUN = cd /home/samuelhdmv/Documentos/face/src && $(RUN)

g ?= ""
gt ?= ""

teste: clear
	@$(ROUTERUN)
	@echo ""

zip: clear
	@rm -f face_print.zip
	@zip -r face_print.zip src
	@echo ""
	@zip -T face_print.zip -v
	@echo ""
	@unzip -l face_print.zip
	@echo ""

rm: clear
	@rm -f /home/samuelhdmv/Documentos/face/src/imgs/*
	@echo ""
	@ls --color=always -alh /home/samuelhdmv/Documentos/face/src/imgs/
	@echo ""

clear:
	clear
	@ls --color=always -alh
	@echo ""

set:
	@echo "$(FILE)"

#Para mexer com git

git: add
	@git push
	@echo ""

add:
ifeq ($(gt),)
	@git add .
	@git commit -m "$(g)"
	@echo ""
else
	@git add .
	@git commit -m "$(g)" -m "$(gt)"
	@echo ""
endif

