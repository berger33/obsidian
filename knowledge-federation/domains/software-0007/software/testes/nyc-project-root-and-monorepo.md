---
id: software.testes.tranche16.001009
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
fontes: ["https://github.com/istanbuljs/nyc", "https://www.npmjs.com/package/nyc"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# nyc: resolver raízes em repositório com múltiplos pacotes

## Em uma frase
A raiz do projeto orienta a busca de fontes, a formação de padrões e a localização dos diretórios de artefato.

## Por que importa
Em repositórios com vários pacotes, uma raiz mal definida faz a ferramenta medir módulos errados ou não encontrar fontes.

## Como funciona
Defina a raiz explicitamente quando o comando partir de subdiretório e confirme os diretórios gerados dentro da estrutura esperada.

## Exemplo
Executar a suíte de um pacote a partir da raiz do repositório exige que os padrões de caminho incluam o prefixo correto do pacote.

## Limites e trade-offs
Dependências compartilhadas e pacotes do espaço de trabalho podem ficar fora da medição por padrão, o que exige decisão explícita sobre os limites do escopo.

## Como verificar
Liste os arquivos instrumentados e confirme que todos pertencem ao pacote sob teste, sem vizinhos incluídos por acidente.

## Conexões
- [[nyc-typescript-and-source-maps]] — Veja também: nyc: ajustar a medição para código transpilado.
- [[nyc-ci-multi-job]] — Veja também: nyc: consolidar cobertura entre trabalhos do pipeline.

## Fontes
- [nyc — repositório oficial](https://github.com/istanbuljs/nyc) — linha de comando, filtros, relatórios, limites e mesclagem de dados; consultado em 2026-10-03.
- [nyc — pacote npm](https://www.npmjs.com/package/nyc) — opções documentadas e exemplos de uso do publicador; consultado em 2026-10-03.
