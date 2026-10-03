---
id: software.testes.tranche24.001765
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://raw.githubusercontent.com/robotframework/robotframework/master/README.rst", "https://github.com/robotframework/robotframework"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Fundação, marca e o duplo licenciamento do projeto

## Em uma frase
O desenvolvimento é patrocinado pela Robot Framework Foundation, entidade sem fins lucrativos — e a marca Robot Framework pertence a ela; o código é Apache License 2.0, enquanto documentação e conteúdo similar usam Creative Commons Attribution 3.0 Unported, e o README avisa que bibliotecas do ecossistema podem adotar licenças diferentes.

## Por que importa
Para empresas, a cadeia de licença importa: copiar material do User Guide para um treinamento exige a atribuição da CC-BY; já o código sob Apache-2.0 permite uso proprietário; e cada biblioteca de terceiro precisa de verificação própria, como o README frisa.

## Como funciona
Ao adotar o framework, registre a fundação como mantenedora, use o código como Apache-2.0 e, se reproduzir documentação, aplique a atribuição CC-BY 3.0; para bibliotecas do ecossistema, verifique a licença em cada repositório antes de incluir no produto.

## Exemplo
Um slide de treinamento que reproduz o texto do User Guide deve creditar conforme CC-BY; o mesmo slide citando código de exemplo de uma biblioteca precisa checar a licença daquela biblioteca, não a do framework.

## Limites e trade-offs
O README cobre a licença do framework e da documentação deste repositório; projetos do ecossistema têm governança própria, e a nota não substitui a leitura de cada LICENSE.

## Como verificar
Conferi as seções "License and Trademark" e "Introduction" (patrocínio da fundação) no README oficial.

## Conexões
- [[robotframework-rebot]] — Veja também: rebot: pós-processamento e junção de resultados.
- [[robotframework-ecosystem]] — Veja também: O ecossistema como parte do produto.

## Fontes
- [Robot Framework README.rst oficial](https://raw.githubusercontent.com/robotframework/robotframework/master/README.rst) — README.rst oficial do Robot Framework com introdução, instalação, exemplo de suíte, CLI robot/rebot, ecossistema, fundação e licenciamento.; consultado em 2026-10-03.
- [Repositório oficial robotframework/robotframework](https://github.com/robotframework/robotframework) — Repositório oficial no GitHub com código-fonte, histórico de commits, branches, tags e canais do projeto.; consultado em 2026-10-03.
