---
id: software.testes.tranche25.001881
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md"
fontes: ["https://gitlab.com/akihe/radamsa/-/raw/master/README.md", "https://gitlab.com/akihe/radamsa"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Abordagem estritamente black-box e origem no Protos Genome Project

## Em uma frase
O README caracteriza o Radamsa como um fuzzer extremamente black-box porque não precisa de nenhuma informação sobre o programa alvo nem sobre o formato dos dados (seja XML ou MP3), tendo nascido como subproduto do Protos Genome Project do OUSPG, que explorava técnicas para inferir modelos de dados com linguagens formais regulares e livres de contexto.

## Por que importa
Fuzzers guiados por cobertura ou baseados em gramática exigem instrumentação do binário ou especificação do protocolo antes do primeiro teste; um mutador black-box que infere estrutura das próprias amostras permite começar a testar qualquer binário fechado ou filtro UNIX em segundos.

## Como funciona
Alimente amostras reais do formato (XML, música, código, arquivos comprimidos) diretamente no Radamsa sem escrever gramática; se quiser refinar uma campanha contínua mais tarde, o README nota que é possível pareá-lo opcionalmente com análise de cobertura para melhorar o conjunto de amostras.

## Exemplo
O mesmo binário radamsa muta expressões aritméticas para bc, expressões Lisp para o compilador ol e streams comprimidos para gzip sem mudar nenhuma configuração de formato.

## Limites e trade-offs
Por ser black-box por padrão, o Radamsa sozinho não sabe quais mutações abriram novos caminhos no alvo; a afirmação do README é pragmática: primeiro pôr os testes para rodar facilmente e depois refinar a técnica se necessário.

## Como verificar
Conferi os parágrafos sobre black-box e sobre o Protos Genome Project na seção What the Fuzz do README oficial.

## Conexões
- [[radamsa-what-it-is]] — Veja também: Radamsa: gerador de casos de teste para testes de robustez.
- [[radamsa-build-single-binary]] — Veja também: Requisitos de SO e build que gera um binário único sem dependências externas.

## Fontes
- [Radamsa — README oficial (A Crash Course to Radamsa)](https://gitlab.com/akihe/radamsa/-/raw/master/README.md) — README oficial do Radamsa com proposta black-box, origem no Protos Genome Project, build de binário único, uso em pipe como cat, semente -s/--seed, mutador numérico, -n e laço de captura de crash.; consultado em 2026-10-03.
- [Repositório oficial akihe/radamsa no GitLab](https://gitlab.com/akihe/radamsa) — Repositório oficial do Radamsa no GitLab com código-fonte, Makefile, mutadores e documentação.; consultado em 2026-10-03.
