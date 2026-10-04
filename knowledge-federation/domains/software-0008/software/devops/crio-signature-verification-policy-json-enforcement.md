---
id: software.devops.tranche04.000376
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/cri-o/cri-o/main/README.md", "https://cri-o.github.io/cri-o", "https://github.com/cri-o/cri-o"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Verificação nativa de assinaturas de imagem no nó Kubernetes com policy.json no CRI-O

## Em uma frase
Como o CRI-O utiliza a biblioteca `container-libs/image`, ele avalia nativamente o arquivo **`policy.json(5)`** (`containers-policy.json`) antes de concluir o pull de qualquer imagem solicitada pelo Kubelet. Isso permite exigir verificação criptográfica de assinaturas (incluindo assinaturas GPG simples e assinaturas Sigstore/Cosign suportadas por `containers/image`) diretamente na camada do runtime de contêiner em cada nó, rejeitando imagens não assinadas ou de registros não autorizados mesmo que um pod tenha escapado de um webhook de admissão no control plane.

## Por que importa
Defesa em profundidade no Kubernetes exige que a verificação de assinatura não dependa apenas de um admission controller na API Server: validar `policy.json` no próprio CRI-O garante que nenhum contêiner não assinado seja iniciado pelo Kubelet no nó.

## Como funciona
Configure `/etc/containers/policy.json` nos nós CRI-O com uma política padrão restritiva (`reject`) e regras explícitas `signedBy` / `sigstoreSigned` para os namespaces e registros OCI aprovados pela organização.

## Exemplo
Em um ambiente financeiro regulado, além da verificação no Kyverno, cada nó trabalhador possui `policy.json` configurado no CRI-O exigindo assinatura Sigstore válida para qualquer imagem puxada de `registry.corp.internal/prod/*`.

## Limites e trade-offs
Cuidado ao aplicar `"default": [{"type": "reject"}]` em `policy.json` sem antes listar explicitamente os repositórios das imagens de sistema do próprio Kubernetes (`registry.k8s.io`), plugins CNI e agentes de monitoramento, sob pena de impedir o bootstrap dos pods de infraestrutura do nó.

## Como verificar
Tente agendar um pod com uma imagem não assinada de um repositório sujeito a regra de assinatura em `policy.json` e confirme nos eventos do pod (`ErrImagePull`) que o CRI-O bloqueou a imagem por violação de política.

## Conexões
- [[crio-http-status-api-and-crio-status-cli]] — Veja também: Inspeção de runtime com crio status e API HTTP sobre socket Unix /var/run/crio/crio.sock.
- [[crio-oci-hooks-injection-and-annotations-migration]] — Veja também: Suporte a OCI Hooks e guia de migração de anotações no CRI-O.

## Fontes
- [CRI-O GitHub — README.md (Kubernetes Compatibility Matrix, Scope, Config & HTTP Status API)](https://raw.githubusercontent.com/cri-o/cri-o/main/README.md) — README oficial do CRI-O detalhando alinhamento de versões 1.x.y e política de version skew n-2 com o Kubernetes, escopo estrito de implementação da CRI para o Kubelet, bibliotecas OCI (runc, container-libs/image, container-libs/storage, CNI), arquivos crio.conf, policy.json, registries.conf, storage.conf e API de status via crio status e socket /var/run/crio/crio.sock.; consultado em 2026-10-03.
- [CRI-O — Official Release Notes & Documentation Portal](https://cri-o.github.io/cri-o) — Portal oficial de notas de versão e relatórios de dependências do CRI-O mantido pelos desenvolvedores do projeto.; consultado em 2026-10-03.
- [CRI-O — Official GitHub Repository](https://github.com/cri-o/cri-o) — Repositório oficial Apache-2.0 do CRI-O na CNCF.; consultado em 2026-10-03.
