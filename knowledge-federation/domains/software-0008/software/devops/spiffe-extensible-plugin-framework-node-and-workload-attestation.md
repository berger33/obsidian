---
id: software.devops.tranche05.000476
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/spiffe/spire/main/README.md", "https://spiffe.io/spire/try/", "https://github.com/spiffe/spire"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Framework extensível de plugins do SPIRE para atestação de nós, workloads e autoridades certificadoras

## Em uma frase
O README oficial aponta para o guia **Extend SPIRE** (`spiffe.io/spire/docs/extending/`) e para a matriz de integrações suportadas (`doc/supported_integrations.md`), destacando o framework altamente extensível de plugins do SPIRE. Tanto o `spire-server` quanto o `spire-agent` operam sobre tipos de plugins modulares: **NodeAttestor** (verifica a identidade física ou virtual do nó, como Kubernetes PSAT, AWS IID, GCP IIT, Azure MSI, TPM ou X.509), **WorkloadAttestor** (inspeciona o processo local no kernel Linux/Unix, Kubernetes Kubelet, Docker ou systemd para descobrir seus seletores), **UpstreamAuthority** (conecta o `spire-server` a uma CA corporativa raiz como HashiCorp Vault, AWS PCA ou cert-manager) e **KeyManager**.

## Por que importa
Essa arquitetura de plugins é o que permite ao SPIRE emitir identidades uniformes tanto para um Pod no Kubernetes (atestado via `k8s_psat` + `k8s` workload attestor) quanto para um binário bare-metal (atestado via certificado de hardware + UID/hash de binário no kernel), encadeando a raiz de confiança na PKI corporativa existente.

## Como funciona
Configure o `NodeAttestor` e o `WorkloadAttestor` adequados a cada plataforma (como `k8s_psat` para nós Kubernetes) e conecte um plugin `UpstreamAuthority` no `spire-server` para que as CAs intermediárias do SPIRE sejam assinadas pela autoridade certificadora raiz da organização.

## Exemplo
Quando um pod inicia em um nó Kubernetes, o plugin `WorkloadAttestor` `k8s` do `spire-agent` consulta o Kubelet local pelo PID do contêiner, confirma que o pod pertence ao namespace `financeiro` com a ServiceAccount `faturamento` e emite o SVID correspondente à entrada registrada no `spire-server`.

## Limites e trade-offs
Evite usar seletores de atestação fracos ou genéricos (como permitir qualquer pod do namespace `default` com a ServiceAccount `default`); combine sempre múltiplos seletores estritos (`k8s:ns:...`, `k8s:sa:...`, imagem ou labels verificadas) ao registrar identidades no SPIRE.

## Como verificar
Inspecione as entradas de registro no `spire-server` (`spire-server entry show`) e valide que os seletores (`Selectors`) exigem o namespace e a ServiceAccount específicos de cada workload.

## Conexões
- [[spiffe-go-spiffe-and-java-spiffe-client-libraries]] — Veja também: Bibliotecas clientes oficiais go-spiffe e java-spiffe para consumo direto da SPIFFE Workload API.
- [[spiffe-scaling-spire-and-federation-deployment-models]] — Veja também: Escalabilidade e modelos de implantação do SPIRE (doc/scaling_spire.md) e federação de Trust Domains.

## Fontes
- [SPIRE GitHub — README.md (SPIFFE Runtime Environment, Workload API, SVIDs, Envoy SDS & Security Audits)](https://raw.githubusercontent.com/spiffe/spire/main/README.md) — README oficial do SPIRE (projeto graduado na CNCF sob Apache-2.0) detalhando implementação de produção do SPIFFE, SPIFFE Workload API, emissão de SPIFFE IDs e SVIDs (X.509 mTLS e JWT), imagens spire-server/spire-agent/oidc-discovery-provider, bibliotecas go-spiffe e java-spiffe, integração com Envoy SDS, framework de plugins e auditorias de segurança Cure53 (2021) e CNCF TAG-Security (2018 e 2020).; consultado em 2026-10-03.
- [SPIFFE & SPIRE Official Documentation — Quickstart Guides & Architecture](https://spiffe.io/spire/try/) — Portal oficial do SPIFFE e SPIRE com arquitetura de atestação de nó e workload, guias para Kubernetes/Linux/macOS e o livro gratuito Solving the Bottom Turtle.; consultado em 2026-10-03.
- [SPIRE — Official GitHub Repository](https://github.com/spiffe/spire) — Repositório oficial Apache-2.0 do SPIRE na CNCF.; consultado em 2026-10-03.
