---
id: software.devops.tranche08.000725
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

# Google gVisor: pilha de rede em espaço de usuário (Netstack) e importação via branch sintética @go

## Em uma frase
O gVisor implementa sua própria pilha de rede TCP/IP em espaço de usuário escrita em Go (`Netstack`, pacote `pkg/tcpip`) e mantém uma branch sintética `@go` para permitir que projetos externos importem subpacotes do gVisor com `go get`.

## Por que importa
Em um sandbox de segurança, permitir que um processo não confiável execute chamadas `socket(2)`, `connect(2)` ou `setsockopt(2)` diretamente contra a pilha de rede do kernel do host expõe dezenas de protocolos e estruturas complexas do kernel a vulnerabilidades de corrupção de memória. Além disso, muitos projetos externos em Go (como clientes VPN, proxies e túneis userspace) precisam reutilizar a pilha TCP/IP em Go do gVisor (`Netstack`). O README oficial do gVisor explica tanto a arquitetura da pilha quanto como importá-la via `go get`.

## Como funciona
Durante a configuração inicial do sandbox (que requer privilégios no host antes que o `runsc` se re-execute e descarte todos os privilégios), o gVisor configura o link de rede virtual e inicializa o **Netstack** dentro do processo Sentry. Todo o processamento de pacotes IP, handshakes TCP, janelas de congestionamento, sockets UDP e tabelas de roteamento do container ocorre em memória segura Go dentro do Sentry. Para desenvolvedores externos que desejam importar pacotes como `pkg/tcpip` em projetos Go padrão (já que a branch `master` usa Bazel e não é compatível diretamente com `@latest` do `go get`), o projeto mantém uma branch sintética chamada `go`, selecionável explicitamente com o sufixo `@go`.

## Exemplo
```bash
# Importar a implementação TCP do Netstack do gVisor em um projeto Go externo usando a branch sintética @go
go get gvisor.dev/gvisor/pkg/tcpip/transport/tcp@go

# Compilar apenas a biblioteca tcpip diretamente no repositório do gVisor
make build TARGETS="//pkg/tcpip:tcpip"
```

## Limites e trade-offs
Conforme adverte a nota em negrito na seção `Using go get` do README oficial do gVisor, **compilar o `runsc` a partir da branch `go` não é suportado**, pois o gVisor e o `runsc` exigem vários binários (alguns dos quais nem sequer são escritos em Go) gerados pelo Bazel para funcionar; a branch `go` é mantida em regime de melhor esforço apenas para consumo de bibliotecas Go, e todo desenvolvimento deve ocorrer na branch `master`.

## Como verificar
Em um módulo Go de teste, execute `go get gvisor.dev/gvisor/pkg/tcpip/transport/tcp@go` e verifique no `go.mod` a resolução bem-sucedida do pseudo-versionamento a partir da branch `go`.

## Conexões
- [[gvisor-defesa-profundidade-limites-protecao-runtime-monitoring]] — Veja também: Google gVisor: modelo de defesa em profundidade, fronteiras do que o gVisor não protege e Runtime Monitoring.
- [[gvisor-build-bazel-docker-testes-macos]] — Veja também: Google gVisor: sistema de build com Bazel/Docker, requisitos (Linux 5.6+) e execução de testes (incluindo macOS).
- [[gvisor-arquitetura-sentry-gofer-application-kernel]] — Referência cruzada direta com gvisor-arquitetura-sentry-gofer-application-kernel.
- [[gvisor-runtime-oci-runsc-docker-kubernetes-containerd]] — Referência cruzada direta com gvisor-runtime-oci-runsc-docker-kubernetes-containerd.

## Fontes
- [Google gVisor GitHub — README.md (Application Kernel, runsc, Bazel Build & @go Branch)](https://raw.githubusercontent.com/google/gvisor/master/README.md) — README oficial do Google gVisor detalhando motivação de isolamento, compilação do tarball de release (runsc, containerd-shim-runsc-v1, gvisor-bin) com Docker/Bazel e importação da pilha Netstack via branch @go; consultado em 2026-10-03.
- [Google gVisor Architecture Guide — Introduction to gVisor Security (Sentry, Gofer, Systrap & KVM)](https://gvisor.dev/docs/architecture_guide/intro/) — Guia oficial de arquitetura de segurança do gVisor explicando reimplementação de syscalls no Sentry em Go, processo sidecar Gofer, plataformas Systrap/KVM e fronteiras de proteção; consultado em 2026-10-03.
- [Google gVisor — Official GitHub Repository](https://github.com/google/gvisor) — Repositório oficial Apache-2.0 do Google gVisor; consultado em 2026-10-03.
