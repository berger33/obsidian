---
id: software.testes.tranche23.001759
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/google/atheris/blob/master/README.md", "https://google.github.io/oss-fuzz/getting-started/new-project-guide/python-lang"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Integração com OSS-Fuzz e o caso dos módulos nativos

## Em uma frase
A seção Integration with OSS-Fuzz oficial declara suporte pleno: "Atheris is fully supported by OSS-Fuzz, Google's continuous fuzzing service for open source projects", com a integração governada pela guide própria do OSS-Fuzz para Python (link new-project-guide/python-lang na doc do serviço) — ou seja, o caminho local do pip até a campanha contínua da Google existe como produto, não como promessa.

## Por que importa
O outro pé do README é o nativo: a seção Fuzzing Native Extensions condiciona a eficácia — "In order for fuzzing native extensions to be effective, your native extensions must be instrumented" — e delega o como para um documento dedicado no próprio repositório, native_extension_fuzzing.md, o mesmo que explica o internal_libfuzzer da API quando o libFuzzer vem de fora.

## Como funciona
A simetria com a doc do Go fuzzing nativo (também suportado pelo OSS-Fuzz, com guide próprio para a linguagem) marca o padrão do ecossistema: o fuzzer da linguagem e o serviço contínuo são documentos separados, cada um mantido pelo seu dono, amarrados por links canônicos dos dois lados.

## Exemplo
Antes de escalar para OSS-Fuzz, valide localmente com o sanitizer: o README declara que "when fuzzing native code" o Atheris pode ser combinado com AddressSanitizer ou UBSAN para pegar bugs extra — a combinação é o payload da seção nativa.

## Limites e trade-offs
Os detalhes do contrato com o OSS-Fuzz (imagens, corpus em escala, triagem) vivem na doc do serviço, não na do fuzzer — a página apenas aponta; e a exigência de instrumentar extensões nativas significa que o build do seu wheel C pode precisar de flags específicas cobertas apenas no documento dedicado, que esta nota não substitui.

## Como verificar
Confirme as duas seções no README oficial: Integration with OSS-Fuzz com o link da guide Python, e Fuzzing Native Extensions com a frase do must e o nome do arquivo de instruções.

## Conexões
- [[atheris-custom-mutator]] — Veja também: Mutators custom: ensinar a gramática sem ensinar gramática.

## Fontes
- [Atheris — README oficial](https://github.com/google/atheris/blob/master/README.md) — definição, instalação, instrumentação, API e mutators custom; consultado em 2026-10-03.
- [OSS-Fuzz — guia para Python](https://google.github.io/oss-fuzz/getting-started/new-project-guide/python-lang) — integração declarada pela seção de OSS-Fuzz do README; consultado em 2026-10-03.
