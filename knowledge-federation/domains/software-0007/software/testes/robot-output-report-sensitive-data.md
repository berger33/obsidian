---
id: software.testes.tranche11.000479
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html", "https://robotframework.org/robotframework/latest/libraries/BuiltIn.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robot Framework: controlar artefatos de saída e dados sensíveis

## Em uma frase
Uma execução Robot gera output.xml e relatórios/logs configuráveis que ajudam a diagnosticar os casos executados.

## Por que importa
Logs com headers, variáveis, screenshots ou corpos podem expor credenciais e dados pessoais mesmo quando a execução ocorre em CI privado.

## Como funciona
Defina retenção e acesso a artifacts, masque valores confidenciais e limite logging detalhado a cenários descartáveis.

## Exemplo
O job salva resultado resumido, mascara token sintético e remove screenshots depois da retenção configurada.

## Limites e trade-offs
Excluir keyword do log ou mascarar console não remove necessariamente segredos que também aparecem em output.xml ou artifacts anexados.

## Como verificar
Pesquise tokens sentinela em todos os arquivos da execução e valide permissões, retenção e descarte no pipeline.

## Conexões
- [[robot-wait-until-keyword-succeeds-idempotência]] — Veja também: Robot Framework: repetir condição observável sem repetir efeito irreversível.

## Fontes
- [Robot Framework 7.5 — User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html) — formato de testes, setups, teardowns, tags, templates, variáveis, libraries e arquivos de saída; consultado em 2026-10-02.
- [Robot Framework 7.5 — BuiltIn library](https://robotframework.org/robotframework/latest/libraries/BuiltIn.html) — keywords incorporadas de fluxo, logging, execução, variáveis e assertions; consultado em 2026-10-02.
