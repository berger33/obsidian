---
id: software.testes.tranche22.001643
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://docs.hoverfly.io/en/latest/pages/tutorials/basic/exportingsimulations/exportingsimulations.html", "https://github.com/SpectoLabs/hoverfly/blob/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hoverfly: exportar filtrando por URL

## Em uma frase
hoverctl export salva as simulações capturadas em arquivos JSON, e o flag --url-pattern aceita string simples ou regex para fatiar o export: um arquivo por recorte de domínio em vez de um amontoado por suíte.

## Por que importa
Simulações compartíveis por time nascem de exports cirúrgicos: o time de checkout grava só o jsontest.com e versiona echo.json limpo no repositório.

## Como funciona
Os comandos documentados: hoverctl export echo.json --url-pattern "echo.jsontest.com" e hoverctl export api.json --url-pattern "(.+).jsontest.com" para todas as subdomínios.

## Exemplo
O export captura apenas o que já trafegou pela sessão de capture; rodar o export antes de exercitar os caminhos gera arquivo vazio ou incompleto silencioso.

## Limites e trade-offs
Se você roda na máquina atrás de um proxy corporativo, a própria doc manda ler o tutorial "Using Hoverfly behind a proxy" antes — a variável de ambiente do sistema interfere.

## Como verificar
Exporte com e sem --url-pattern na mesma sessão e compare os conjuntos de pares request/response nos dois JSONs.

## Conexões
- [[hoverfly-capture-mode]] — Veja também: Hoverfly: capture grava o tráfego real.
- [[hoverfly-stateful-capture]] — Veja também: Hoverfly: sequências para APIs com estado.

## Fontes
- [Hoverfly — Creating and exporting a simulation](https://docs.hoverfly.io/en/latest/pages/tutorials/basic/exportingsimulations/exportingsimulations.html) — capture mode, proxy 8500, headers e export --url-pattern; consultado em 2026-10-03.
- [Hoverfly — README oficial](https://github.com/SpectoLabs/hoverfly/blob/master/README.md) — proposta, quickstart, build em Go e contribuição; consultado em 2026-10-03.
