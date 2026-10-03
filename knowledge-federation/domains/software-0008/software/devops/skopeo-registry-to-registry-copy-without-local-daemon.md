---
id: software.devops.tranche06.000543
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

# Promoção e cópia direta de imagens entre registros com skopeo copy sem daemon local

## Em uma frase
Na seção *Copying images*, o README oficial demonstra como o subcomando **`skopeo-copy(1)`** (`skopeo copy`) copia uma imagem completa (manifesto, camadas de sistema de arquivos e assinaturas) diretamente de uma localização para outra — por exemplo, de um registro público para um registro corporativo interno com **`skopeo copy docker://quay.io/buildah/stable docker://registry.internal.company.com/buildah`** — sem exigir privilégios de root e sem precisar importar a imagem para um daemon Docker local no meio do caminho.

## Por que importa
No fluxo tradicional com Docker (`docker pull` + `docker tag` + `docker push`), o host precisa rodar um daemon Docker privilegiado, descomprimir todas as camadas no disco local e recomprimi-las para enviá-las ao segundo registro (podendo inclusive alterar digests). O `skopeo copy` transfere os blobs diretamente em streaming mantendo a integridade criptográfica original.

## Como funciona
Substitua sequências de `docker pull` / `docker tag` / `docker push` nos seus pipelines de promoção de artefatos (dev -> staging -> prod) por `skopeo copy` (utilizando `--all` quando desejar copiar todas as arquiteturas de uma manifest list multi-arch).

## Exemplo
Quando uma imagem construída no registro de homologação passa em todos os testes, o job de promoção executa `skopeo copy docker://staging.registry.corp/app@sha256:... docker://prod.registry.corp/app:v2.1.0` em segundos, sem daemon Docker no runner.

## Limites e trade-offs
Ao copiar imagens entre dois registros diferentes que exigem credenciais distintas na mesma execução, utilize as flags separadas **`--src-creds=usuario:token`** e **`--dest-creds=usuario:token`** documentadas no README.

## Como verificar
Execute `skopeo copy` entre dois diretórios ou registros de teste e confirme com `skopeo inspect` que o digest do manifesto copiado permanece idêntico.

## Conexões
- [[skopeo-six-container-storage-and-registry-transports]] — Veja também: Os seis mecanismos de transporte de imagem e armazenamento suportados pelo Skopeo.
- [[skopeo-air-gapped-mirroring-with-skopeo-sync]] — Veja também: Sincronização de repositórios para ambientes desconectados (air-gapped) com skopeo sync.

## Fontes
- [Skopeo GitHub — README.md (Daemonless & Rootless Image Operations, 6 Storage Transports, Inspect, Copy, Sync & Auth)](https://raw.githubusercontent.com/containers/skopeo/main/README.md) — README oficial do Skopeo (Apache-2.0) detalhando operações em imagens OCI e Docker v2 sem exigir root nem daemon, os 6 tipos de transporte (containers-storage:, dir:, docker://, docker-archive:, docker-daemon:, oci:), inspeção remota sem pull (skopeo inspect e --config), cópia entre registros/transportes (skopeo copy), sincronização air-gapped (skopeo sync), autenticação ($XDG_RUNTIME_DIR/containers/auth.json, --creds, --src-creds, --dest-creds), alerta contra sites falsos não afiliados e tabela dos 11 subcomandos CLI.; consultado em 2026-10-03.
- [Skopeo Official Container Image — containers/image_build/skopeo/README.md](https://github.com/containers/image_build/blob/main/skopeo/README.md) — Documentação oficial da imagem de contêiner upstream do Skopeo publicada em quay.io/skopeo/stable.; consultado em 2026-10-03.
- [Skopeo — Official GitHub Repository](https://github.com/containers/skopeo) — Repositório oficial Apache-2.0 do Skopeo (única fonte upstream oficial junto à imagem quay.io/skopeo/stable).; consultado em 2026-10-03.
