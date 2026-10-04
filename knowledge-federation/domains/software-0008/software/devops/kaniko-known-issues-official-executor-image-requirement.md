---
id: software.devops.tranche06.000553
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

# Limitações conhecidas do Kaniko: proibição de copiar o binário executor para outras imagens (como agentes Jenkins)

## Em uma frase
A seção *Known Issues* do README oficial emite um alerta enfático: **executar o Kaniko dentro de qualquer imagem Docker diferente da imagem oficial `gcr.io/kaniko-project/executor` NÃO é suportado devido a detalhes de implementação** — e isso inclui explicitamente **copiar os executáveis do Kaniko da imagem oficial para dentro de outra imagem (por exemplo, uma imagem customizada de agente Jenkins CI)**. O README explica a razão técnica: como o contêiner não deve exigir privilégios, ele não pode usar `chroot` nem `bind-mount`, de modo que **descompacta a imagem base diretamente na própria raiz `/` do contêiner e pode sobrescrever qualquer arquivo que já esteja lá** fora de `/kaniko`. Além disso, o Kaniko não suporta construir contêineres Windows nem a Registry API v1 depreciada.

## Por que importa
Muitos engenheiros tentam criar uma "super-imagem" de agente de CI copiando `/kaniko/executor` para dentro de uma imagem Ubuntu/Jenkins; na primeira execução de build, o Kaniko extrai a imagem base por cima de `/usr` e `/lib` do agente, destruindo o ambiente do contêiner no meio do job.

## Como funciona
Em pipelines Jenkins, GitLab CI ou Tekton no Kubernetes, defina o Kaniko como um **contêiner separado dedicado** dentro do Pod do agente (usando a imagem original `gcr.io/kaniko-project/executor` ou `gcr.io/kaniko-project/executor:debug`), compartilhando o workspace do código via volume Kubernetes (`emptyDir` ou PVC).

## Exemplo
Em um Pod de build do Jenkins no Kubernetes, o contêiner `jnlp` faz o checkout do código no volume compartilhado `/workspace` e o contêiner separado `kaniko` (`gcr.io/kaniko-project/executor:debug`) executa `/kaniko/executor --context=dir:///workspace` com isolamento perfeito do seu rootfs.

## Limites e trade-offs
Nunca faça `COPY --from=gcr.io/kaniko-project/executor /kaniko/executor /usr/local/bin/` para rodar o Kaniko diretamente dentro de um container compartilhado com outras ferramentas.

## Como verificar
Verifique nos templates de Pod do seu sistema de CI que o contêiner que executa `/kaniko/executor` utiliza diretamente a imagem oficial do executor sem mesclá-la a outros agentes.

## Conexões
- [[kaniko-how-kaniko-works-base-image-extraction-and-userspace-snapshotting]] — Veja também: Como o Kaniko funciona: extração da imagem base e snapshotting do sistema de arquivos em userspace.
- [[kaniko-seven-build-context-sources-and-prefixes]] — Veja também: Os sete contextos de build suportados pelo Kaniko (dir, tar, stdin, gs, s3, https Azure e git).

## Fontes
- [Kaniko GitHub — README.md (Archival Notice, Userspace Dockerfile Execution, Build Contexts, Caching & Known Issues)](https://raw.githubusercontent.com/GoogleContainerTools/kaniko/main/README.md) — README oficial do Kaniko (GoogleContainerTools/kaniko) registrando o aviso no topo de que o projeto está arquivado e não é mais mantido, seu funcionamento por extração do rootfs e snapshotting em userspace sem daemon Docker dentro de gcr.io/kaniko-project/executor, os 7 contextos de build suportados, cache de camadas (--cache, --cache-repo) e cache de imagens base (gcr.io/kaniko-project/warmer), execução em Kubernetes/gVisor e limitações conhecidas.; consultado em 2026-10-03.
- [Kaniko GitHub — Getting Started Tutorial (docs/tutorial.md)](https://github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md) — Tutorial histórico oficial de uso do Kaniko em clusters Kubernetes.; consultado em 2026-10-03.
- [Kaniko — Official GitHub Repository (Archived)](https://github.com/GoogleContainerTools/kaniko) — Repositório oficial Apache-2.0 arquivado do Kaniko em GoogleContainerTools.; consultado em 2026-10-03.
