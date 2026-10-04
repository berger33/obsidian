---
id: software.seguranca.tranche16.001534
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

# Gerenciando Falsos Positivos de Bibliotecas de Terceiros no Valgrind com **Suppression Files (`--gen-suppressions=all` e `--suppressions=arquivo.supp`)**

## Em uma frase
Você colocou `valgrind --error-exitcode=1` no pipeline de CI/CD da sua aplicação C/C++, mas uma biblioteca externa fechada ou driver gráfico (`libssl`, `libX11`, `libGL` ou uma biblioteca legada do sistema operacional) gera um aviso conhecido que você não pode corrigir porque não é dono daquela biblioteca. Como silenciar **apenas aquele erro específico naquela pilha de chamadas da biblioteca externa** mantendo a verificação estrita no 100% restante do seu código?

## Por que importa
Usando um **Arquivo de Supressão do Valgrind (`--suppressions=terceiros.supp`)**, documentado na seção 4.4 do `mc-manual.html`!

## Como funciona
E você não precisa escrever a sintaxe do arquivo `.supp` manualmente: basta rodar uma vez o Valgrind com **`--gen-suppressions=all`**! O Valgrind imprimirá no terminal, logo abaixo do erro, o bloco `{ <insert_a_suppression_name_here> Memcheck:Cond ... }` pronto para você copiar, dar um nome descritivo, salvar em `ci/valgrind.supp` e versionar no Git!

## Exemplo
```bash
# Gerar automaticamente os blocos de supressao (--gen-suppressions=all) e executar o gate de CI aplicando o arquivo de supressao versionado
valgrind --tool=memcheck --gen-suppressions=all ./meu_binario 2>&1 | tee ./valgrind_raw.log
valgrind --tool=memcheck --suppressions=./ci/valgrind.supp --error-exitcode=1 ./meu_binario
```

## Limites e trade-offs
Olhe a anatomia de uma regra dentro do arquivo `.supp` explicada no manual oficial: ela especifica a ferramenta e o tipo de erro (ex.: `Memcheck:Leak`, `Memcheck:Addr4`, `Memcheck:Value8`, `Memcheck:Cond`, `Memcheck:Param`) seguido pelos frames da pilha de chamadas (`fun:nome_funcao` ou `obj:/usr/lib/libfoo.so*`, suportando curingas `*`, `?` e **`...`** para pular múltiplos frames intermediários)!

## Como verificar
Regra de ouro de segurança ao revisar Pull Requests que alteram o arquivo `ci/valgrind.supp`: **NUNCA permita uma supressão genérica com `...` que englobe funções do próprio código da sua aplicação** — restrinja o bloco `.supp` estritamente aos símbolos `fun:`/`obj:` da biblioteca externa de terceiros!

## Conexões
- [[valgrind-deteccao-memory-leaks-definitely-indirectly-possibly-lost]] — Veja também: Taxonomia de Vazamentos de Memória (**Memory Leaks**) no Valgrind Memcheck: **`definitely lost`**, **`indirectly lost`**, **`possibly lost`** e **`still reachable`**.
- [[valgrind-inspecao-interativa-vgdb-gdbserver-monitor-commands-leak-check]] — Veja também: Inspeção de Vazamentos e Memória **Em Tempo Real (Sem Parar o Daemon)** no Valgrind via **`vgdb`** e **GDB Remote Monitor (`--vgdb=yes`)**.
- [[valgrind-arquitetura-instrumentacao-binaria-vex-ir-memcheck-valid-bits]] — Referência cruzada direta com valgrind-arquitetura-instrumentacao-binaria-vex-ir-memcheck-valid-bits.
- [[depcheck-tratamento-falsos-positivos-suppression-xml-cpe-cve-purl]] — Referência cruzada direta com depcheck-tratamento-falsos-positivos-suppression-xml-cpe-cve-purl.

## Fontes
- [The Valgrind Quick Start Guide (`valgrind.org/docs/manual/QuickStart.html`)](https://valgrind.org/docs/manual/QuickStart.html) — guia rápido oficial do Valgrind cobrindo preparação de programas (`-g -O1`) e execução sob a ferramenta padrão `Memcheck`; consultado em 2026-10-03.
- [Valgrind User Manual — Memcheck: a memory error detector (`mc-manual.html`)](https://valgrind.org/docs/manual/mc-manual.html) — manual técnico oficial do Memcheck detalhando erros de leitura/escrita inválida, bits `V` (*Valid-Value*) e `A` (*Valid-Address*), `--track-origins=yes`, taxonomia de leaks, `.supp`, `vgdb` e Memory Pools; consultado em 2026-10-03.
