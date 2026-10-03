---
id: software.devops.tranche06.000548
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

# Interoperabilidade direta com o backend containers-storage de Podman, Buildah e CRI-O

## Em uma frase
O README oficial destaca que o transporte **`containers-storage:docker-reference`** opera diretamente sobre uma imagem localizada no store local `containers/storage`, cuja localização e parâmetros são definidos em **`/etc/containers/storage.conf`** — exatamente o mesmo backend utilizado por **Podman (`podman.io`), CRI-O (`cri-o.io`) e Buildah (`buildah.io`)**.

## Por que importa
Essa integração nativa significa que, em um nó Kubernetes que utiliza o runtime **CRI-O** ou em uma estação de trabalho que utiliza **Podman/Buildah**, o administrador pode usar `skopeo copy` para pré-carregar imagens de um diretório local `oci:`/`dir:` diretamente para dentro do `containers-storage:` do nó ou copiar imagens do store local para um registro remoto sem levantar nenhum serviço extra.

## Como funciona
Em nós Kubernetes baseados em CRI-O que precisam de pré-carregamento (pre-warming) de imagens pesadas durante o provisionamento da máquina (por exemplo via Packer), utilize `skopeo copy` apontando o destino para `containers-storage:` para gravar as imagens diretamente onde o CRI-O as consome.

## Exemplo
Durante o build de uma imagem de nó Kubernetes com Packer e CRI-O, o script provisionador executa `skopeo copy oci:/tmp/pause-bundle:3.9 containers-storage:registry.k8s.io/pause:3.9`, deixando as imagens essenciais já disponíveis no cache local do CRI-O antes mesmo do nó entrar no cluster.

## Limites e trade-offs
Ao acessar `containers-storage:` do sistema (`/var/lib/containers/storage` usado pelo CRI-O ou Podman rootful), execute o comando sob o mesmo privilégio/namespace de usuário do proprietário do store e não corrompa os arquivos internos editando `/var/lib/containers` manualmente fora das ferramentas da suíte `containers`.

## Como verificar
Copie uma imagem local para `containers-storage:` em ambiente de teste e confirme que ela aparece imediatamente em `podman images` ou `buildah images`.

## Conexões
- [[skopeo-manifest-digest-computation-and-sigstore-key-tools]] — Veja também: Cálculo local de digest (skopeo manifest-digest) e ferramentas locais de assinatura (generate-sigstore-key, standalone-sign e standalone-verify).
- [[skopeo-official-upstream-sources-and-fake-website-warning]] — Veja também: Alerta de segurança upstream do Skopeo: ausência de site separado e rejeição de sites falsos não afiliados.

## Fontes
- [Skopeo GitHub — README.md (Daemonless & Rootless Image Operations, 6 Storage Transports, Inspect, Copy, Sync & Auth)](https://raw.githubusercontent.com/containers/skopeo/main/README.md) — README oficial do Skopeo (Apache-2.0) detalhando operações em imagens OCI e Docker v2 sem exigir root nem daemon, os 6 tipos de transporte (containers-storage:, dir:, docker://, docker-archive:, docker-daemon:, oci:), inspeção remota sem pull (skopeo inspect e --config), cópia entre registros/transportes (skopeo copy), sincronização air-gapped (skopeo sync), autenticação ($XDG_RUNTIME_DIR/containers/auth.json, --creds, --src-creds, --dest-creds), alerta contra sites falsos não afiliados e tabela dos 11 subcomandos CLI.; consultado em 2026-10-03.
- [Skopeo Official Container Image — containers/image_build/skopeo/README.md](https://github.com/containers/image_build/blob/main/skopeo/README.md) — Documentação oficial da imagem de contêiner upstream do Skopeo publicada em quay.io/skopeo/stable.; consultado em 2026-10-03.
- [Skopeo — Official GitHub Repository](https://github.com/containers/skopeo) — Repositório oficial Apache-2.0 do Skopeo (única fonte upstream oficial junto à imagem quay.io/skopeo/stable).; consultado em 2026-10-03.
