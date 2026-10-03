---
id: software.testes.tranche15.000885
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://pestphp.com/docs/tia", "https://pestphp.com/docs/continuous-integration"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pest 5: manter Tia como aceleração local e suíte completa como contrato de CI

## Em uma frase
Tia usa informação de cobertura para relacionar testes a arquivos e selecionar os casos afetados por mudanças; a primeira execução precisa estabelecer o baseline que guiará as próximas.

## Por que importa
O modo seletivo economiza ciclos no desenvolvimento sem prometer substituir a validação completa do branch.

## Como funciona
A recomendação oficial é deixar `--tia` fora do comando regular de CI e executar a suíte inteira contra checkout limpo, reservando a gravação compartilhada de baseline a um fluxo dedicado.

## Exemplo
Instale PCOV ou Xdebug, rode o comando completo para criar o baseline e use `pest --tia` em iterações locais; configure um workflow específico para atualizar e distribuir baseline se o time adotar esse processo.

## Limites e trade-offs
Sem driver de cobertura, baseline válido ou dependências corretas, seleção incremental pode deixar de executar casos importantes; alterações de configuração compartilhada exigem cautela adicional.

## Como verificar
Altere um arquivo de produção e um arquivo de teste, observe a lista afetada pelo Tia e compare periodicamente com execução completa no mesmo commit.

## Conexões
- [[pest-parallel-nao-isola-recursos-externos]] — Veja também: Pest 5: desenhar testes independentes antes de habilitar parallel.
- [[pest-tia-elegibilidade-e-cobertura-dos-casos-reproduzidos]] — Veja também: Pest 5: interpretar a cobertura preservada por Tia como trilha reproduzível.

## Fontes
- [Pest 5 — Tia Engine](https://pestphp.com/docs/tia) — baseline de impact analysis, driver de cobertura, testes afetados e replay; consultado em 2026-10-02.
- [Pest 5 — Continuous Integration](https://pestphp.com/docs/continuous-integration) — execução integral em CI, browser plugin, parallel e artifacts; consultado em 2026-10-02.
