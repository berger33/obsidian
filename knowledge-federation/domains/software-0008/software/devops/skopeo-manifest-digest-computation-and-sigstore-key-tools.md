---
id: software.devops.tranche06.000547
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

# Cálculo local de digest (skopeo manifest-digest) e ferramentas locais de assinatura (generate-sigstore-key, standalone-sign e standalone-verify)

## Em uma frase
A tabela completa de subcomandos ao final do README oficial documenta quatro utilitários criptográficos e de verificação embutidos no Skopeo: **`skopeo-manifest-digest(1)`** (`skopeo manifest-digest`, que calcula o digest criptográfico de um arquivo de manifesto local e o escreve na saída padrão), **`skopeo-generate-sigstore-key(1)`** (`skopeo generate-sigstore-key`, que gera um par de chaves pública/privada sigstore), **`skopeo-standalone-sign(1)`** (ferramenta de depuração para assinar uma imagem localmente sem fazer upload) e **`skopeo-standalone-verify(1)`** (ferramenta de depuração para verificar uma assinatura de imagem a partir de arquivos locais).

## Por que importa
Quando imagens e manifestos são transportados como diretórios (`dir:` ou `oci:`) através de mídias offline para ambientes air-gapped, calcular o digest localmente com `skopeo manifest-digest` e testar assinaturas offline com `standalone-sign` / `standalone-verify` permite validar a integridade do manifesto sem precisar de conexão com um servidor de registro HTTP.

## Como funciona
Use `skopeo manifest-digest manifest.json` ao inspecionar diretórios `dir:` exportados para comprovar que o arquivo `manifest.json` local corresponde exatamente ao digest `sha256:...` aprovado pela equipe de segurança.

## Exemplo
Após exportar uma imagem com `skopeo copy docker://... dir:/tmp/img`, o operador executa `skopeo manifest-digest /tmp/img/manifest.json` e compara o hash SHA-256 calculado com o digest original do registro.

## Limites e trade-offs
Como o próprio README indica na descrição de `skopeo-standalone-sign` e `skopeo-standalone-verify`, esses dois subcomandos específicos são ferramentas de depuração local; para assinatura e verificação em registros remotos em fluxos produtivos, utilize as flags de assinatura integradas ao `skopeo copy` / `containers-policy.json` ou o `cosign`.

## Como verificar
Execute `skopeo manifest-digest` sobre o arquivo `manifest.json` de uma imagem exportada em formato `dir:` e confirme que o hash impresso bate com o campo `.Digest` do `skopeo inspect`.

## Conexões
- [[skopeo-deleting-images-and-registry-garbage-collection]] — Veja também: Marcação de imagens para exclusão em registros com skopeo delete e coleta de lixo.
- [[skopeo-containers-storage-interoperability-with-podman-buildah-crio]] — Veja também: Interoperabilidade direta com o backend containers-storage de Podman, Buildah e CRI-O.

## Fontes
- [Skopeo GitHub — README.md (Daemonless & Rootless Image Operations, 6 Storage Transports, Inspect, Copy, Sync & Auth)](https://raw.githubusercontent.com/containers/skopeo/main/README.md) — README oficial do Skopeo (Apache-2.0) detalhando operações em imagens OCI e Docker v2 sem exigir root nem daemon, os 6 tipos de transporte (containers-storage:, dir:, docker://, docker-archive:, docker-daemon:, oci:), inspeção remota sem pull (skopeo inspect e --config), cópia entre registros/transportes (skopeo copy), sincronização air-gapped (skopeo sync), autenticação ($XDG_RUNTIME_DIR/containers/auth.json, --creds, --src-creds, --dest-creds), alerta contra sites falsos não afiliados e tabela dos 11 subcomandos CLI.; consultado em 2026-10-03.
- [Skopeo Official Container Image — containers/image_build/skopeo/README.md](https://github.com/containers/image_build/blob/main/skopeo/README.md) — Documentação oficial da imagem de contêiner upstream do Skopeo publicada em quay.io/skopeo/stable.; consultado em 2026-10-03.
- [Skopeo — Official GitHub Repository](https://github.com/containers/skopeo) — Repositório oficial Apache-2.0 do Skopeo (única fonte upstream oficial junto à imagem quay.io/skopeo/stable).; consultado em 2026-10-03.
