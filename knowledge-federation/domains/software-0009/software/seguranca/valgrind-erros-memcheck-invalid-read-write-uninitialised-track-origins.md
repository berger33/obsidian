---
id: software.seguranca.tranche16.001532
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://valgrind.org/docs/manual/QuickStart.html", "https://valgrind.org/docs/manual/mc-manual.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Interpretando Erros Críticos do **Memcheck**: `Invalid read/write`, `Use of uninitialised value` (**`--track-origins=yes`**), `Syscall param` e `Invalid free()` / `Mismatched free()`

## Em uma frase
Quando o **Valgrind Memcheck** analisa um serviço C/C++ e imprime mensagens como **`Invalid write of size 4`**, **`Conditional jump or move depends on uninitialised value(s)`**, **`Syscall param write(buf) points to uninitialised byte(s)`** ou **`Mismatched free() / delete / delete []`**, qual é o impacto de segurança de cada uma dessas classes documentadas na seção 4.2 do `mc-manual.html`?

## Por que importa
Veja o mapa direto para vulnerabilidades reais: **(1) `Invalid read / Invalid write of size N`** — é um **Heap Out-of-Bounds (Buffer Overflow / Over-read)** ou **Use-After-Free (`Address 0x... is 0 bytes inside a block of size 64 free'd`)**! O Memcheck mostra tanto o stack trace do acesso ilegal quanto o stack trace exato de onde o bloco foi alocado ou liberado!

## Como funciona
**(2) `Syscall param write(buf) points to uninitialised byte(s)`** — uma vulnerabilidade clássica de **Information Disclosure (Vazamento de Memória / Infoleak)**, onde uma `struct` em C com bytes de *padding* não zerados na stack ou no heap é enviada diretamente pela rede (`send`/`write`) ou gravada em disco! E **(3) `Invalid free()` / `Mismatched free()`** — **Double-Free** ou mistura incorreta entre `new[]` do C++ e `free()`/`delete` escalar!

## Exemplo
```bash
# Executar o Valgrind Memcheck rastreando a origem exata de valores nao inicializados (--track-origins=yes) e falhando com exit code 99 se achar erro
valgrind \
  --tool=memcheck \
  --track-origins=yes \
  --read-var-info=yes \
  --error-exitcode=99 \
  ./servidor_teste --self-test
```

## Limites e trade-offs
Olhe as 3 flags de ouro no comando acima: **(1) `--track-origins=yes`** mostra exatamente em qual linha do código a variável de stack ou o bloco `malloc` que originou o valor não inicializado foi criado!; **(2) `--read-var-info=yes`** lê as informações DWARF do binário para dizer o nome exato da variável local ou global envolvida no erro; e **(3) `--error-exitcode=99`** faz o Valgrind retornar código de saída `99` se detectar **qualquer erro de memória**, quebrando imediatamente o pipeline de CI/CD!

## Como verificar
Se o seu código aloca uma `struct` em C que será enviada pela rede ou copiada para espaço de usuário via `ioctl`/`write`, use sempre `memset(&s, 0, sizeof(s))` (ou `calloc`) para zerar também os bytes invisíveis de alinhamento (*struct padding*) entre os campos!

## Conexões
- [[valgrind-arquitetura-instrumentacao-binaria-vex-ir-memcheck-valid-bits]] — Veja também: Arquitetura do **Valgrind (`valgrind 3.27+`)** e do Motor **Memcheck**: Instrumentação Dinâmica via **VEX IR** e Máquina de Sombra de Bits **`V` (*Valid-Value*)** e **`A` (*Valid-Address*)**.
- [[valgrind-deteccao-memory-leaks-definitely-indirectly-possibly-lost]] — Veja também: Taxonomia de Vazamentos de Memória (**Memory Leaks**) no Valgrind Memcheck: **`definitely lost`**, **`indirectly lost`**, **`possibly lost`** e **`still reachable`**.

## Fontes
- [The Valgrind Quick Start Guide (`valgrind.org/docs/manual/QuickStart.html`)](https://valgrind.org/docs/manual/QuickStart.html) — guia rápido oficial do Valgrind cobrindo preparação de programas (`-g -O1`) e execução sob a ferramenta padrão `Memcheck`; consultado em 2026-10-03.
- [Valgrind User Manual — Memcheck: a memory error detector (`mc-manual.html`)](https://valgrind.org/docs/manual/mc-manual.html) — manual técnico oficial do Memcheck detalhando erros de leitura/escrita inválida, bits `V` (*Valid-Value*) e `A` (*Valid-Address*), `--track-origins=yes`, taxonomia de leaks, `.supp`, `vgdb` e Memory Pools; consultado em 2026-10-03.
