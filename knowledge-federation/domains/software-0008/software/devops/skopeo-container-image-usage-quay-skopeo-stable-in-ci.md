---
id: software.devops.tranche06.000550
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
fontes: ["https://raw.githubusercontent.com/containers/skopeo/main/README.md", "https://github.com/containers/image_build/blob/main/skopeo/README.md", "https://github.com/containers/skopeo"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Execução do Skopeo em contêiner (quay.io/skopeo/stable) para pipelines CI/CD e Tekton Tasks

## Em uma frase
O README oficial e a página dedicada `containers/image_build/blob/main/skopeo/README.md` documentam o uso do Skopeo empacotado como imagem oficial de contêiner em **`quay.io/skopeo/stable`**. Como o Skopeo não exige daemon nem privilégios de root para operações de rede (`inspect`, `list-tags`, `copy` entre registros `docker://`, `sync` e `delete`), a imagem `quay.io/skopeo/stable` pode ser executada em pods Kubernetes com `securityContext` altamente restrito (`runAsNonRoot: true`, `allowPrivilegeEscalation: false`, sem montar sockets do nó).

## Por que importa
Em plataformas cloud-native de CI/CD como Tekton Pipelines, Argo Workflows, GitHub Actions e GitLab CI sobre Kubernetes, usar `quay.io/skopeo/stable` para inspecionar digests, promover imagens entre registros e sincronizar catálogos mantém o cluster totalmente livre de containers privilegiados.

## Como funciona
Configure suas Tasks de promoção e inspeção de imagens nos pipelines de CI/CD utilizando a imagem oficial `quay.io/skopeo/stable` (preferencialmente fixada por tag e `@sha256` digest) montando apenas o Secret de credenciais do registro (`auth.json`).

## Exemplo
Uma Tekton Task de promoção de release executa `quay.io/skopeo/stable` como usuário não-root, lê as credenciais de um Kubernetes Secret montado e executa `skopeo copy` da imagem homologada para o registro de produção.

## Limites e trade-offs
Ao usar `quay.io/skopeo/stable` apenas para operações entre registros remotos (`docker://` -> `docker://`) ou diretórios (`dir:` / `oci:`), nenhum privilégio especial é necessário; privilégios adicionais de user namespace só seriam relevantes se o contêiner tentasse manipular camadas complexas em `containers-storage:` local.

## Como verificar
Execute um contêiner efêmero de teste com `quay.io/skopeo/stable` rodando `skopeo inspect docker://quay.io/skopeo/stable` e confirme o retorno do manifesto sem exigir flags privilegiadas.

## Conexões
- [[skopeo-official-upstream-sources-and-fake-website-warning]] — Veja também: Alerta de segurança upstream do Skopeo: ausência de site separado e rejeição de sites falsos não afiliados.

## Fontes
- [Skopeo GitHub — README.md (Daemonless & Rootless Image Operations, 6 Storage Transports, Inspect, Copy, Sync & Auth)](https://raw.githubusercontent.com/containers/skopeo/main/README.md) — README oficial do Skopeo (Apache-2.0) detalhando operações em imagens OCI e Docker v2 sem exigir root nem daemon, os 6 tipos de transporte (containers-storage:, dir:, docker://, docker-archive:, docker-daemon:, oci:), inspeção remota sem pull (skopeo inspect e --config), cópia entre registros/transportes (skopeo copy), sincronização air-gapped (skopeo sync), autenticação ($XDG_RUNTIME_DIR/containers/auth.json, --creds, --src-creds, --dest-creds), alerta contra sites falsos não afiliados e tabela dos 11 subcomandos CLI.; consultado em 2026-10-03.
- [Skopeo Official Container Image — containers/image_build/skopeo/README.md](https://github.com/containers/image_build/blob/main/skopeo/README.md) — Documentação oficial da imagem de contêiner upstream do Skopeo publicada em quay.io/skopeo/stable.; consultado em 2026-10-03.
- [Skopeo — Official GitHub Repository](https://github.com/containers/skopeo) — Repositório oficial Apache-2.0 do Skopeo (única fonte upstream oficial junto à imagem quay.io/skopeo/stable).; consultado em 2026-10-03.
