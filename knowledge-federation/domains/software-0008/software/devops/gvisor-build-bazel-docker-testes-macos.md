---
id: software.devops.tranche08.000726
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

# Google gVisor: sistema de build com Bazel/Docker, requisitos (Linux 5.6+) e execução de testes (incluindo macOS)

## Em uma frase
O gVisor compila em arquiteturas `x86_64` e `ARM64` (exigindo Linux 5.6+ e Docker 17.09.0+ para o container de build que encapsula o Bazel), oferecendo alvos `make unit-tests`, `make tests` e suporte a testes de análise estática no macOS com `bazel@8`.

## Por que importa
Como o gVisor combina código Go do kernel de aplicação, código C/C++/Assembly de baixo nível das plataformas de interceptação e múltiplos binários sidecar (`runsc`, `containerd-shim-runsc-v1`, `gvisor-bin/`), reproduzir o ambiente exato de compiladores e ferramentas em diferentes máquinas de desenvolvedores exige um sistema de build hermético. A seção `Installing from source` do README oficial do gVisor documenta o uso via Makefile/Docker e via Bazel/Bazelisk direto.

## Como funciona
O fluxo recomendado encapsula o **Bazel** e todas as dependências de compilação dentro de um container Docker de build (definido em `images/default/Dockerfile`), bastando ter **Linux 5.6+** e **Docker 17.09.0+** e rodar `make release-tarball DESTINATION=bin/`, `make unit-tests` ou `make test TARGETS="//runsc:version_test"`. Caso o desenvolvedor deseje usar o Bazel diretamente sem Docker, deve instalar as dependências listadas no Dockerfile e usar o **Bazelisk** (ou a versão exata em `.bazelversion`) executando `bazel build -c opt //debian:gvisor-release-tar-bz2`. No macOS, é possível rodar testes de ferramentas e analisadores (`//tools/nogo/...`, `//tools/check{aligned,const,escape,linkname,locks,unsafe}/...`) instalando `brew install bazel@8` e passando `--macos_sdk_version=$(xcrun --show-sdk-version)`.

## Exemplo
```bash
# Executar um alvo específico de teste do runsc usando o wrapper Makefile ou diretamente com Bazel
make test TARGETS="//runsc:version_test"
bazel test //runsc:version_test
```

## Limites e trade-offs
Conforme observa o README oficial do gVisor (`Building directly with Bazel`), usar o Bazel diretamente no host sem o wrapper do Makefile/Docker não é recomendado para a maioria dos usuários devido à sobrecarga extra de configurar e manter manualmente todas as dependências de sistema e toolchains listadas em `images/default/Dockerfile`.

## Como verificar
Verifique a versão requerida do Bazel no arquivo `.bazelversion` do repositório do gVisor e execute `make test TARGETS="//runsc:version_test"` para validar a pipeline de compilação e teste.

## Conexões
- [[gvisor-pilha-rede-userspace-netstack-importacao-branch-go]] — Veja também: Google gVisor: pilha de rede em espaço de usuário (Netstack) e importação via branch sintética @go.
- [[gvisor-isolamento-sistema-arquivos-gofer-mount-namespaces]] — Veja também: Google gVisor: isolamento de sistema de arquivos com o processo sidecar Gofer, VFS em Go e pivot_root.
- [[gvisor-arquitetura-sentry-gofer-application-kernel]] — Referência cruzada direta com gvisor-arquitetura-sentry-gofer-application-kernel.
- [[gvisor-runtime-oci-runsc-docker-kubernetes-containerd]] — Referência cruzada direta com gvisor-runtime-oci-runsc-docker-kubernetes-containerd.

## Fontes
- [Google gVisor GitHub — README.md (Application Kernel, runsc, Bazel Build & @go Branch)](https://raw.githubusercontent.com/google/gvisor/master/README.md) — README oficial do Google gVisor detalhando motivação de isolamento, compilação do tarball de release (runsc, containerd-shim-runsc-v1, gvisor-bin) com Docker/Bazel e importação da pilha Netstack via branch @go; consultado em 2026-10-03.
- [Google gVisor Architecture Guide — Introduction to gVisor Security (Sentry, Gofer, Systrap & KVM)](https://gvisor.dev/docs/architecture_guide/intro/) — Guia oficial de arquitetura de segurança do gVisor explicando reimplementação de syscalls no Sentry em Go, processo sidecar Gofer, plataformas Systrap/KVM e fronteiras de proteção; consultado em 2026-10-03.
- [Google gVisor — Official GitHub Repository](https://github.com/google/gvisor) — Repositório oficial Apache-2.0 do Google gVisor; consultado em 2026-10-03.
