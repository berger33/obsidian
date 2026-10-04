---
id: software.testes.tranche25.001882
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

# Requisitos de SO e build que gera um binário único sem dependências externas

## Em uma frase
As seções Requirements e Building Radamsa listam os sistemas operacionais suportados — GNU/Linux, OpenBSD, FreeBSD, Mac OS X e Windows (via Cygwin) — e as ferramentas para compilar a partir do código-fonte (gcc ou clang, make, git e wget); após git clone, cd radamsa e make, o resultado em bin/radamsa é um único arquivo binário sem dependências externas.

## Por que importa
Um fuzzer que compila para um único executável autossuficiente pode ser copiado diretamente para máquinas de teste, contêineres enxutos ou ambientes de staging sem instalar runtimes, bibliotecas dinâmicas ou pacotes no sistema alvo.

## Como funciona
Clone o repositório oficial, execute make e instale com sudo make install ou simplesmente copie o binário bin/radamsa para onde precisar e remova o restante da árvore de compilação; confirme com radamsa --help.

## Exemplo
Em um contêiner de CI mínimo, basta copiar o executável bin/radamsa já compilado para /usr/local/bin/radamsa e invocá-lo nos scripts de teste.

## Limites e trade-offs
No Windows, o suporte listado pelo README depende de Cygwin; o documento não promete build nativo fora desse ambiente na seção Requirements.

## Como verificar
Conferi as seções Requirements e Building Radamsa no README oficial do projeto.

## Conexões
- [[radamsa-black-box-and-protos-origin]] — Veja também: Abordagem estritamente black-box e origem no Protos Genome Project.
- [[radamsa-unix-cat-pipe-model]] — Veja também: O modelo mental do cat UNIX que quebra dados no caminho.

## Fontes
- [Radamsa — README oficial (A Crash Course to Radamsa)](https://gitlab.com/akihe/radamsa/-/raw/master/README.md) — README oficial do Radamsa com proposta black-box, origem no Protos Genome Project, build de binário único, uso em pipe como cat, semente -s/--seed, mutador numérico, -n e laço de captura de crash.; consultado em 2026-10-03.
- [Repositório oficial akihe/radamsa no GitLab](https://gitlab.com/akihe/radamsa) — Repositório oficial do Radamsa no GitLab com código-fonte, Makefile, mutadores e documentação.; consultado em 2026-10-03.
