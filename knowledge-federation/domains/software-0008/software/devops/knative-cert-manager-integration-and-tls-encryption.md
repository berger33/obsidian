---
id: software.devops.tranche05.000467
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
fontes: ["https://raw.githubusercontent.com/knative/serving/main/README.md", "https://raw.githubusercontent.com/knative/serving/main/DEVELOPMENT.md", "https://github.com/knative/serving"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Integração do Knative Serving com cert-manager para provisionamento automático de certificados TLS

## Em uma frase
No roteiro oficial de inicialização em `DEVELOPMENT.md`, antes de implantar o Knative Serving, implanta-se o **`cert-manager`** (`kubectl apply -f ./third_party/cert-manager-latest/cert-manager.yaml`) aguardando que todos os CRDs estejam `Established` (`kubectl wait --for=condition=Established --all crd`) e que todos os Deployments no namespace `cert-manager` estejam `Available` (`kubectl wait --for=condition=Available -n cert-manager --all deployments`). Essa base permite que o Knative Serving (através de componentes como `serving-nscert.yaml` / integração com `cert-manager`) provisione automaticamente certificados TLS para as rotas externas (auto-TLS) e para criptografia interna do tráfego.

## Por que importa
Aplicações serverless expostas pelo Knative Serving criam URLs dinâmicas por serviço e por namespace (`https://<service>.<namespace>.<domain>`). Integrar o Knative ao `cert-manager` automatiza a emissão e renovação de certificados X.509 para cada rota criada sem intervenção manual.

## Como funciona
Garanta que o `cert-manager` esteja instalado, saudável e com seus CRDs e webhooks disponíveis antes de habilitar recursos de certificados automáticos (`serving-nscert.yaml` / `auto-tls`) no Knative Serving.

## Exemplo
Quando um desenvolvedor cria um novo Knative `Service`, o controlador do Knative solicita um recurso `Certificate` ao `cert-manager` para o domínio do serviço, aguarda a emissão do Secret TLS e configura o gateway de entrada para servir HTTPS automaticamente.

## Limites e trade-offs
Nunca aplique manifestos que criam recursos do `cert-manager` antes de aguardar `kubectl wait --for=condition=Available -n cert-manager --all deployments`, pois o webhook do `cert-manager` rejeitará ou falhará na validação enquanto seus pods ainda estiverem iniciando.

## Como verificar
Verifique com `kubectl get kcert` (Knative Certificates) e `kubectl get certificate -A` a emissão limpa dos certificados TLS para as rotas do Knative Serving.

## Conexões
- [[knative-ko-build-tool-and-local-registries-ko-local-kind-local]] — Veja também: Desenvolvimento e deploy de imagens Go no Knative com a ferramenta ko (ko.local, kind.local e --platform).
- [[knative-webhook-validation-and-defaulting-in-knative]] — Veja também: Papel do pod webhook na validação, atribuição de defaults e conversão de recursos no Knative Serving.

## Fontes
- [Knative Serving GitHub — README.md (Serverless Containers, Scale to Zero, Routing & Point-in-Time Snapshots)](https://raw.githubusercontent.com/knative/serving/main/README.md) — README oficial do Knative Serving (Apache-2.0) descrevendo primitivas de middleware sobre Kubernetes para deploy rápido de contêineres serverless, escalonamento automático até zero (scale to zero), roteamento/programação de rede e snapshots point-in-time de código e configuração.; consultado em 2026-10-03.
- [Knative Serving GitHub — DEVELOPMENT.md (Prerequisites, ko, Cert-Manager, Manifests & Core Pods)](https://raw.githubusercontent.com/knative/serving/main/DEVELOPMENT.md) — Guia oficial de desenvolvimento e arquitetura de implantação do Knative Serving detalhando ferramentas (Go, ko, kubectl, protoc), KO_DOCKER_REPO (ko.local/kind.local), dimensionamento de recursos (6 CPUs/8GB single-node ou 4 CPUs/8GB 3-node), manifestos serving-crds.yaml/serving-core.yaml/serving-hpa.yaml/serving-nscert.yaml e pods activator, autoscaler, autoscaler-hpa, controller e webhook em knative-serving.; consultado em 2026-10-03.
- [Knative Serving — Official GitHub Repository](https://github.com/knative/serving) — Repositório oficial Apache-2.0 do Knative Serving na CNCF.; consultado em 2026-10-03.
