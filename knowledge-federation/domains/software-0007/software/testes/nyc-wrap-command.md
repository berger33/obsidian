---
id: software.testes.tranche16.001002
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://github.com/istanbuljs/nyc", "https://github.com/istanbuljs/istanbuljs"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# nyc: instrumentar um comando existente

## Em uma frase
A ferramenta envolve o comando informado, instrumentando os módulos carregados durante a execução e gravando dados brutos em diretório temporário.

## Por que importa
Instrumentar por envolvimento dispensa alterar o código do projeto e mantém a medição próxima da execução real.

## Como funciona
Coloque o comando da suíte como argumento da ferramenta, mantenha o diretório temporário fora do controle de versão e gere o relatório a partir dos dados coletados.

## Exemplo
Envolver o comando de testes faz com que os módulos exigidos pela suíte sejam registrados sem intervenção no código de produção.

## Limites e trade-offs
Processos filhos podem não ser instrumentados automaticamente, e testes que iniciam outro processo exigem configuração adicional.

## Como verificar
Compare a lista de arquivos do relatório com a estrutura esperada do projeto para identificar módulos que ficaram fora.

## Conexões
- [[nyc-all-and-filters]] — Veja também: nyc: incluir arquivos não carregados.

## Fontes
- [nyc — repositório oficial](https://github.com/istanbuljs/nyc) — linha de comando, filtros, relatórios, limites e mesclagem de dados; consultado em 2026-10-03.
- [Istanbul — monorepo oficial](https://github.com/istanbuljs/istanbuljs) — instrumentação JavaScript, bibliotecas de cobertura e geradores de relatório; consultado em 2026-10-03.
