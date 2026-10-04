---
id: software.devops.tranche08.000730
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/google/gvisor/master/README.md", "https://gvisor.dev/docs/architecture_guide/intro/", "https://github.com/google/gvisor"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Google gVisor: verificadores estáticos de código Go (nogo), governança, ADOPTERS.md e política de segurança

## Em uma frase
O repositório do gVisor aplica verificadores estáticos rigorosos sobre seu próprio código Go (`//tools/nogo/...` e `//tools/check{aligned,const,escape,linkname,locks,unsafe}/...`) e documenta sua governança (`GOVERNANCE.md`), usuários em produção (`ADOPTERS.md`) e política de segurança (`SECURITY.md`).

## Por que importa
Embora a linguagem Go seja memory-safe por padrão, um kernel de aplicação como o gVisor precisa utilizar blocos específicos de `unsafe`, alinhamento de memória, locks concorrentes complexos e controle estrito de alocação na heap (escape analysis) para implementar chamadas de sistema com alta performance; um erro de concorrência ou de ponteiro `unsafe` no Sentry poderia introduzir vulnerabilidades. O README oficial do gVisor revela as ferramentas internas de verificação que auditam essas propriedades no CI.

## Como funciona
Durante o build e os testes via Bazel, o gVisor executa a infraestrutura **`nogo`** (`//tools/nogo/...`) junto a uma suíte de analisadores estáticos customizados em `//tools/checkaligned`, `//tools/checkconst`, `//tools/checkescape`, `//tools/checklinkname`, `//tools/checklocks` e `//tools/checkunsafe`. Esses analisadores garantem em tempo de compilação que invariantes críticas do kernel Sentry — como a ordem correta de aquisição e liberação de mutexes (`checklocks`), a ausência de escapes inesperados de memória em caminhos quentes (`checkescape`) e o alinhamento seguro de estruturas (`checkaligned`) — sejam respeitadas. Na camada comunitária, `GOVERNANCE.md`, `ADOPTERS.md` e `SECURITY.md` regem a manutenção do projeto e o reporte privado de vulnerabilidades.

## Exemplo
```bash
# Executar os analisadores estáticos nogo e checadores de invariantes do kernel gVisor com Bazel
bazel test //tools/nogo/... //tools/checkaligned/... //tools/checklocks/... //tools/checkunsafe/...
```

## Limites e trade-offs
As anotações estritas exigidas pelos verificadores internos do gVisor (como anotações `+checklocks` e `+checkescape` nos comentários das funções Go do Sentry) tornam a contribuição de código ao núcleo do gVisor mais rigorosa do que em projetos Go comuns, pois qualquer violação de lock ou alocação não autorizada falha imediatamente o build do Bazel.

## Como verificar
Consulte os diretórios `tools/nogo` e `tools/checklocks` no repositório `google/gvisor` e verifique a execução dos testes de análise estática com `bazel test`.

## Conexões
- [[gvisor-modos-privilegio-reexecucao-rootless-network-none]] — Veja também: Google gVisor: modelo de privilégios na inicialização do runsc, queda de privilégios e modo rootless.
- [[gvisor-arquitetura-sentry-gofer-application-kernel]] — Referência cruzada direta com gvisor-arquitetura-sentry-gofer-application-kernel.
- [[gvisor-build-bazel-docker-testes-macos]] — Referência cruzada direta com gvisor-build-bazel-docker-testes-macos.
- [[gvisor-defesa-profundidade-limites-protecao-runtime-monitoring]] — Referência cruzada direta com gvisor-defesa-profundidade-limites-protecao-runtime-monitoring.

## Fontes
- [Google gVisor GitHub — README.md (Application Kernel, runsc, Bazel Build & @go Branch)](https://raw.githubusercontent.com/google/gvisor/master/README.md) — README oficial do Google gVisor detalhando motivação de isolamento, compilação do tarball de release (runsc, containerd-shim-runsc-v1, gvisor-bin) com Docker/Bazel e importação da pilha Netstack via branch @go; consultado em 2026-10-03.
- [Google gVisor Architecture Guide — Introduction to gVisor Security (Sentry, Gofer, Systrap & KVM)](https://gvisor.dev/docs/architecture_guide/intro/) — Guia oficial de arquitetura de segurança do gVisor explicando reimplementação de syscalls no Sentry em Go, processo sidecar Gofer, plataformas Systrap/KVM e fronteiras de proteção; consultado em 2026-10-03.
- [Google gVisor — Official GitHub Repository](https://github.com/google/gvisor) — Repositório oficial Apache-2.0 do Google gVisor; consultado em 2026-10-03.
