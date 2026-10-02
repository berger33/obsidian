---
id: software.testes.tranche12.000559
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
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://playwright.dev/docs/test-reporters", "https://playwright.dev/docs/test-configuration"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Playwright Test: selecionar reporters por finalidade

## Em uma frase
O runner inclui reporters com níveis de detalhe distintos e permite configurar mais de um para a mesma execução.

## Por que importa
Saída concisa em CI e detalhes interativos em desenvolvimento atendem usos diferentes; um arquivo JSON separado também permite integração automatizada sem interpretar texto de terminal.

## Como funciona
Defina `reporter` no config ou pela CLI, combine os formatos necessários e forneça caminhos de saída que sobrevivam à limpeza do job. Evite ativar formatos pesados em toda execução sem consumidor definido.

## Exemplo
Uma equipe pode usar `list` localmente e um reporter compacto na CI, além de salvar JSON com resultados quando uma etapa posterior o consome.

## Limites e trade-offs
Adicionar reporters não garante retenção do arquivo no provedor de CI, e anexar simultaneamente formatos redundantes pode aumentar armazenamento sem melhorar diagnóstico.

## Como verificar
Verifique a saída terminal e a existência dos arquivos gerados em execução local e em job de CI representativo; confirme também se a pipeline publica os artefatos esperados.

## Conexões
- [[playwright-test-step-relatorio]] — Veja também: Playwright Test: steps nomeados para tornar falhas legíveis.

## Fontes
- [Playwright — Reporters](https://playwright.dev/docs/test-reporters) — reporters integrados, múltiplos formatos e configuração em CI; consultado em 2026-10-02.
- [Playwright — Test configuration](https://playwright.dev/docs/test-configuration) — configuração de testDir, projetos, expect, retries, workers e artefatos; consultado em 2026-10-02.
