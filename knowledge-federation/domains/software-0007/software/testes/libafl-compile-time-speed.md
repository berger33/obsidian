---
id: software.testes.tranche24.001802
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
fontes: ["https://raw.githubusercontent.com/AFLplusplus/LibAFL/main/README.md", "https://github.com/AFLplusplus/LibAFL"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Overhead mínimo por decisão de compilação

## Em uma frase
O primeiro destaque do README é "fast": a filosofia declarada é fazer "everything we can at compile time, keeping runtime overhead minimal", e o número de prova é o relato de usuários — 120k execs/sec em frida-mode num telefone, usando todos os núcleos.

## Por que importa
Framework de biblioteca tem dois custos possíveis: abstração em runtime ou código gerado no build; o LibAFL escolhe o segundo explicitamente, o que torna aceitável usá-lo no loop mais quente da pesquisa (milhões de execuções/dia por core).

## Como funciona
Trate o compile-time como contrato de arquitetura: os componentes são tipos genéricos compostos no seu binário, não objetos despachados dinamicamente — por isso a doc de API online (docs.rs/libafl) e a leitura dos exemplos valem mais que configuração em YAML.

## Exemplo
O número do README é particularmente revelador pelo contexto: um telefone — não um servidor de benchmark — sustentando 120 mil execuções por segundo com instrumentação de Frida.

## Limites e trade-offs
"Users reach" é relato de usuários citado pelo projeto, não garantia; o README não especifica o modelo do telefone nem a configuração do run.

## Como verificar
O bullet "fast" da lista de destaques do README oficial define a filosofia e cita o número.

## Conexões
- [[libafl-llmp-scaling]] — Veja também: LLMP: escala quase linear por núcleo e TCP entre máquinas.
- [[libafl-custom-inputs]] — Veja também: BytesInput é opcional: o formato de input é seu.

## Fontes
- [LibAFL — README oficial](https://raw.githubusercontent.com/AFLplusplus/LibAFL/main/README.md) — README oficial do LibAFL com conceitos centrais, LLMP, backends de instrumentação, no_std, dependências LLVM/Rust, exemplos em fuzzers/ e citação CCS '22.; consultado em 2026-10-03.
- [Repositório oficial AFLplusplus/LibAFL](https://github.com/AFLplusplus/LibAFL) — Repositório oficial do LibAFL no GitHub com crates modulares, exemplos em fuzzers/, livro mdBook e guias de depuração/contribuição.; consultado em 2026-10-03.
