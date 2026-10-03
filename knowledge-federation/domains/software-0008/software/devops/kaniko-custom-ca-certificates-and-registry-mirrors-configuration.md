---
id: software.devops.tranche06.000560
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

# Configuração de certificados CA privados (/kaniko/ssl/certs/), mTLS de registro e registry mirrors no Kaniko

## Em uma frase
Para operar em redes corporativas com autoridades certificadoras (CAs) internas, inspeção TLS ou espelhos de registros públicos, o README oficial documenta as montagens e flags de rede do Kaniko: certificados CA customizados podem ser montados como um `ConfigMap` diretamente em **`/kaniko/ssl/certs/`** (como demonstrado no manifesto Kubernetes oficial de exemplo) ou apontados por registro via **`--registry-certificate my.registry.name=/path/to/the/certificate.cert`** (além de certificados clientes mTLS via **`--registry-client-cert`**), enquanto espelhos para evitar rate-limits ou tráfego externo são configurados com **`--registry-mirror`** e **`--registry-map`** (acompanhados de `--skip-default-registry-fallback` quando o acesso ao registro público original deve ser bloqueado).

## Por que importa
Ao invés de recorrer a flags inseguras como `--insecure` ou `--skip-tls-verify` para contornar erros `x509: certificate signed by unknown authority` ao acessar o Harbor/Artifactory interno da empresa, montar o pacote de CAs corporativas em `/kaniko/ssl/certs/` mantém a validação criptográfica TLS 100% ativa.

## Como funciona
Monte o `ConfigMap` contendo o bundle de CAs corporativas em `/kaniko/ssl/certs/` (ou use `--registry-certificate`) e configure `--registry-mirror=mirror.corp.internal` para acelerar o pull de imagens base do Docker Hub e evitar limites de taxa (`429 Too Many Requests`).

## Exemplo
Em uma empresa com registro interno assinado por PKI própria e sem acesso direto ao Docker Hub nos runners, o template do pod Kaniko monta o `cabundle` em `/kaniko/ssl/certs/` e passa `--registry-mirror=harbor.corp.internal/dockerhub-proxy --skip-default-registry-fallback`.

## Limites e trade-offs
Evite usar `--insecure`, `--insecure-pull` ou `--skip-tls-verify` em pipelines de produção, pois desabilitar a verificação TLS expõe o build a ataques Man-in-the-Middle na injeção de imagens base.

## Como verificar
Execute um build no Kaniko puxando uma imagem base através do `--registry-mirror` configurado com TLS verificado por `/kaniko/ssl/certs/` e confirme o sucesso nos logs.

## Conexões
- [[kaniko-multi-arch-container-manifests-with-manifest-tool]] — Veja também: Construção de imagens multi-arquitetura (multi-arch) combinando Kaniko e manifest-tool.

## Fontes
- [Kaniko GitHub — README.md (Archival Notice, Userspace Dockerfile Execution, Build Contexts, Caching & Known Issues)](https://raw.githubusercontent.com/GoogleContainerTools/kaniko/main/README.md) — README oficial do Kaniko (GoogleContainerTools/kaniko) registrando o aviso no topo de que o projeto está arquivado e não é mais mantido, seu funcionamento por extração do rootfs e snapshotting em userspace sem daemon Docker dentro de gcr.io/kaniko-project/executor, os 7 contextos de build suportados, cache de camadas (--cache, --cache-repo) e cache de imagens base (gcr.io/kaniko-project/warmer), execução em Kubernetes/gVisor e limitações conhecidas.; consultado em 2026-10-03.
- [Kaniko GitHub — Getting Started Tutorial (docs/tutorial.md)](https://github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md) — Tutorial histórico oficial de uso do Kaniko em clusters Kubernetes.; consultado em 2026-10-03.
- [Kaniko — Official GitHub Repository (Archived)](https://github.com/GoogleContainerTools/kaniko) — Repositório oficial Apache-2.0 arquivado do Kaniko em GoogleContainerTools.; consultado em 2026-10-03.
