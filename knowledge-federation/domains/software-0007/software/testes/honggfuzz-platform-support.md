---
id: software.testes.tranche24.001795
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
fontes: ["https://raw.githubusercontent.com/google/honggfuzz/master/README.md", "https://github.com/google/honggfuzz/blob/master/docs/USAGE.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Seis famílias de SO: do Linux ao Windows via Cygwin

## Em uma frase
A seção de features declara "Broad Support: Linux, macOS, Android, NetBSD, FreeBSD, and Windows (Cygwin)" — o fuzzer roda no kernel Linux e nos BSDs, cobre Android e exige a camada Cygwin para Windows.

## Por que importa
Suporte multiplataforma permite fuzzar o mesmo alvo onde a bug-hunt rende: bibliotecas portáveis nos três sistemas para pegar bugs de compilação específica, e Android como casa de componentes em produção real.

## Como funciona
Instale dependências por SO (no Ubuntu/Debian: binutils-dev, libunwind-dev, libblocksruntime-dev e clang), rode "make" — que gera os wrappers em hfuzz_cc/ — e use o mesmo binário em cada plataforma-alvo.

## Exemplo
O bloco de Instalação do README lista o apt-get completo para Debian/Ubuntu e o requisito de Xcode 10.8+ com libblocksruntime para macOS: build idiomático por plataforma, sem script único.

## Limites e trade-offs
Windows é coberto "Cygwin" apenas, como o parêntese do README deixa claro; comportamento nativo MSVC não é o que a feature listada afirma.

## Como verificar
A lista de plataformas e as dependências por SO constam das seções Key Features e Installation do README oficial.

## Conexões
- [[honggfuzz-ptrace-monitoring]] — Veja também: ptrace: detectar sinais sequestrados e crashes escondidos.
- [[honggfuzz-build-wrappers]] — Veja também: O build: make, hfuzz_cc e os wrappers de compilação.

## Fontes
- [Honggfuzz — README oficial](https://raw.githubusercontent.com/google/honggfuzz/master/README.md) — README oficial do Honggfuzz com recursos de cobertura por hardware/software, modo persistente, ptrace, build wrappers, placeholder ___FILE___ e trophies.; consultado em 2026-10-03.
- [Honggfuzz — USAGE.md no repositório oficial](https://github.com/google/honggfuzz/blob/master/docs/USAGE.md) — Documento oficial USAGE.md do Honggfuzz com opções detalhadas de execução, cobertura e monitoramento.; consultado em 2026-10-03.
