---
id: software.devops.tranche06.000556
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/GoogleContainerTools/kaniko/main/README.md", "https://github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md", "https://github.com/GoogleContainerTools/kaniko"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Execução segura do Kaniko em clusters Kubernetes e dentro do sandbox gVisor (runsc --force)

## Em uma frase
A seção *Running kaniko* do README oficial documenta a execução do Kaniko tanto em um **cluster Kubernetes padrão** (como um `Pod` com `restartPolicy: Never` que monta o segredo de autenticação do registro de destino) quanto dentro do sandbox de segurança de contêineres **[gVisor](https://github.com/google/gvisor)** (`--runtime=runsc`). O README destaca um detalhe técnico indispensável para o gVisor: para rodar o Kaniko sob gVisor é obrigatório adicionar a flag **`--force`**, pois atualmente não há uma forma padrão de o verificador interno determinar automaticamente se o processo está rodando dentro de um contêiner gVisor.

## Por que importa
Executar builds de código submetido por dezenas de desenvolvedores ou PRs externos dentro de um sandbox **gVisor (`runsc`)** adiciona uma fronteira extra de isolamento de chamadas de sistema (kernel em userspace) ao redor do contêiner Kaniko.

## Como funciona
Em clusters Kubernetes que utilizam `RuntimeClass` baseada em gVisor (`runsc`) para isolar pods de CI/CD, adicione a flag `--force` aos argumentos (`args`) do contêiner `gcr.io/kaniko-project/executor`.

## Exemplo
Para isolar completamente os builds de CI em um cluster multi-tenant, a plataforma agenda os pods do Kaniko com a `RuntimeClass` do gVisor e inclui `--force` nos argumentos do executor conforme documentado no README oficial.

## Limites e trade-offs
Lembre-se de definir `restartPolicy: Never` (em Pods diretos) ou `backoffLimit` controlado (em Jobs Kubernetes) ao executar o Kaniko, para que um erro de sintaxe no `Dockerfile` do desenvolvedor falhe imediatamente no pipeline em vez de reiniciar o pod em loop infinito.

## Como verificar
Teste um build de exemplo em um pod Kubernetes com `restartPolicy: Never` (e `--force` se estiver sob runtime `runsc`) confirmando o término com status `Completed` (`Exit Code: 0`).

## Conexões
- [[kaniko-remote-layer-caching-and-base-image-warmer]] — Veja também: Cache remoto de camadas (--cache, --cache-repo) e pré-aquecimento local de imagens base (kaniko warmer).
- [[kaniko-registry-authentication-docker-hub-gcr-ecr-and-acr]] — Veja também: Configuração de autenticação do Kaniko para Docker Hub, Google GCR, Amazon ECR, Azure ACR e JFrog.

## Fontes
- [Kaniko GitHub — README.md (Archival Notice, Userspace Dockerfile Execution, Build Contexts, Caching & Known Issues)](https://raw.githubusercontent.com/GoogleContainerTools/kaniko/main/README.md) — README oficial do Kaniko (GoogleContainerTools/kaniko) registrando o aviso no topo de que o projeto está arquivado e não é mais mantido, seu funcionamento por extração do rootfs e snapshotting em userspace sem daemon Docker dentro de gcr.io/kaniko-project/executor, os 7 contextos de build suportados, cache de camadas (--cache, --cache-repo) e cache de imagens base (gcr.io/kaniko-project/warmer), execução em Kubernetes/gVisor e limitações conhecidas.; consultado em 2026-10-03.
- [Kaniko GitHub — Getting Started Tutorial (docs/tutorial.md)](https://github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md) — Tutorial histórico oficial de uso do Kaniko em clusters Kubernetes.; consultado em 2026-10-03.
- [Kaniko — Official GitHub Repository (Archived)](https://github.com/GoogleContainerTools/kaniko) — Repositório oficial Apache-2.0 arquivado do Kaniko em GoogleContainerTools.; consultado em 2026-10-03.
