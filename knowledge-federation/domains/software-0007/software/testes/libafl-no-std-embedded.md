---
id: software.testes.tranche24.001804
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

# no_std: fuzzador dentro de firmware e hypervisor

## Em uma frase
O destaque "multi platform" enumera Windows, macOS, iOS, Linux e Android, e acrescenta o caso extremo: "LibAFL can be built in no_std mode to inject LibAFL into obscure targets like embedded devices and hypervisors" — o framework cabe em ambientes Rust sem a biblioteca padrão.

## Por que importa
Fuzzar bare-metal é historicamente "compile o fuzzer separado e reze"; a construção no_std move o motor para dentro do próprio firmware, o que permite coverage-feedback em targets onde nem SO nem processo existem do jeito convencional.

## Como funciona
Configure o crate com no_std para o alvo de destino, seguindo os padrões dos exemplos multi-plataforma, e trate o transporte do corpus como problema seu — a engine roda no dispositivo, o gerenciamento dos dados continua na máquina de trabalho.

## Exemplo
Hypervisors e dispositivos embarcados são os dois exemplos que o README nomeia como "obscure targets" — o caso de uso não é retórico, é a razão declarada do modo.

## Limites e trade-offs
O modo no_std exige que o alvo seja Rust (ou integrado a ele) e a nota não cobre exemplos específicos de firmware; o README lista a capacidade, o livro WIP e os exemplos é que mostram o caminho real por plataforma.

## Como verificar
A frase do no_std e a lista de plataformas estão no bullet "multi platform" do README oficial.

## Conexões
- [[libafl-custom-inputs]] — Veja também: BytesInput é opcional: o formato de input é seu.
- [[libafl-instrumentation-backends]] — Veja também: Quatro backends de instrumentação declarados.

## Fontes
- [LibAFL — README oficial](https://raw.githubusercontent.com/AFLplusplus/LibAFL/main/README.md) — README oficial do LibAFL com conceitos centrais, LLMP, backends de instrumentação, no_std, dependências LLVM/Rust, exemplos em fuzzers/ e citação CCS '22.; consultado em 2026-10-03.
- [Repositório oficial AFLplusplus/LibAFL](https://github.com/AFLplusplus/LibAFL) — Repositório oficial do LibAFL no GitHub com crates modulares, exemplos em fuzzers/, livro mdBook e guias de depuração/contribuição.; consultado em 2026-10-03.
