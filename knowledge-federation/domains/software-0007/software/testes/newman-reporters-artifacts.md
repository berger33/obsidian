---
id: software.testes.tranche12.000637
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
fontes: ["https://github.com/postmanlabs/newman/blob/develop/README.md#reporters", "https://github.com/postmanlabs/newman/blob/develop/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Newman: combinar reporters sem perder saída CLI

## Em uma frase
Reporters integrados podem gerar saída terminal, JSON ou JUnit, e selecionar reporters de arquivo pode alterar se o reporter CLI continua habilitado.

## Por que importa
Formato legível por máquina integra resultados com CI, enquanto a saída terminal ajuda a diagnosticar execução local sem abrir artefatos.

## Como funciona
Configure `--reporters` explicitamente, inclua `cli` quando também quiser saída de console e forneça um caminho de exportação para cada arquivo publicado.

## Exemplo
Um job pode emitir JUnit para o painel da pipeline e JSON para análise automatizada mantendo `cli` visível durante o desenvolvimento local.

## Limites e trade-offs
Declarar somente reporter de arquivo pode remover a saída terminal esperada; caminhos não publicados fazem o relatório desaparecer quando o job termina.

## Como verificar
Execute uma collection com dois formatos, verifique ambos os arquivos e confira o output do processo que o sistema de CI realmente captura.

## Conexões
- [[newman-timeout-scopes]] — Veja também: Newman: distinguir timeout total, de request e de script.
- [[newman-custom-reporter-package]] — Veja também: Newman: estender relatórios com reporter externo.

## Fontes
- [Newman — Reporters](https://github.com/postmanlabs/newman/blob/develop/README.md#reporters) — reporters integrados, saídas CLI/JSON/JUnit e exportação de resultados; consultado em 2026-10-02.
- [Newman — README e opções](https://github.com/postmanlabs/newman/blob/develop/README.md) — estado de manutenção, CLI, opções, reporters e uso como biblioteca; consultado em 2026-10-02.
