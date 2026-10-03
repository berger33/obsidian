---
id: software.devops.tranche06.000546
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

# Marcação de imagens para exclusão em registros com skopeo delete e coleta de lixo

## Em uma frase
Na tabela de comandos e exemplos do README oficial, o subcomando **`skopeo-delete(1)`** (`skopeo delete docker://localhost:5000/imagename:latest`) é descrito com precisão técnica: ele **marca o nome/manifesto da imagem para exclusão posterior pelo coletor de lixo (garbage collector) do registro**.

## Por que importa
Muitos administradores executam `skopeo delete` em um registro privado Docker Distribution / OCI esperando que o espaço em disco do servidor do registro diminua no mesmo segundo; porém, na arquitetura de registros V2, a chamada de API `DELETE` remove apenas a referência do manifesto, e os blobs das camadas em disco só são fisicamente apagados quando o processo de *garbage collection* do registro é executado.

## Como funciona
Utilize `skopeo delete` em scripts de retenção para remover manifestos de imagens temporárias de pull requests ou builds antigos, e agende a execução periódica do garbage collector no seu servidor de registro (Harbor, Quay, Distribution) para recuperar o espaço físico em disco.

## Exemplo
Ao encerrar e mesclar um pull request, o workflow de limpeza executa `skopeo delete` sobre a imagem de preview daquele PR no registro privado, deixando os blobs órfãos prontos para a janela diária de coleta de lixo do registro.

## Limites e trade-offs
Tenha extrema cautela com `skopeo delete`: na API V2 de registros, a exclusão opera internamente pelo **digest do manifesto**; se duas tags diferentes (por exemplo `:v1.2.0` e `:latest`) apontarem para exatamente o mesmo digest naquele repositório, deletar uma delas removerá o manifesto subjacente para ambas.

## Como verificar
Verifique com `skopeo inspect` que a referência deletada em um registro de teste não está mais acessível após `skopeo delete`.

## Conexões
- [[skopeo-authentication-flows-login-auth-json-and-creds-flags]] — Veja também: Gerenciamento de autenticação em registros com skopeo login, auth.json e flags --creds, --src-creds e --dest-creds.
- [[skopeo-manifest-digest-computation-and-sigstore-key-tools]] — Veja também: Cálculo local de digest (skopeo manifest-digest) e ferramentas locais de assinatura (generate-sigstore-key, standalone-sign e standalone-verify).

## Fontes
- [Skopeo GitHub — README.md (Daemonless & Rootless Image Operations, 6 Storage Transports, Inspect, Copy, Sync & Auth)](https://raw.githubusercontent.com/containers/skopeo/main/README.md) — README oficial do Skopeo (Apache-2.0) detalhando operações em imagens OCI e Docker v2 sem exigir root nem daemon, os 6 tipos de transporte (containers-storage:, dir:, docker://, docker-archive:, docker-daemon:, oci:), inspeção remota sem pull (skopeo inspect e --config), cópia entre registros/transportes (skopeo copy), sincronização air-gapped (skopeo sync), autenticação ($XDG_RUNTIME_DIR/containers/auth.json, --creds, --src-creds, --dest-creds), alerta contra sites falsos não afiliados e tabela dos 11 subcomandos CLI.; consultado em 2026-10-03.
- [Skopeo Official Container Image — containers/image_build/skopeo/README.md](https://github.com/containers/image_build/blob/main/skopeo/README.md) — Documentação oficial da imagem de contêiner upstream do Skopeo publicada em quay.io/skopeo/stable.; consultado em 2026-10-03.
- [Skopeo — Official GitHub Repository](https://github.com/containers/skopeo) — Repositório oficial Apache-2.0 do Skopeo (única fonte upstream oficial junto à imagem quay.io/skopeo/stable).; consultado em 2026-10-03.
