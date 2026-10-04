---
id: software.devops.tranche05.000472
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

# Documentos de identidade verificáveis SVIDs (X.509 e JWT) para mTLS e autenticação entre serviços

## Em uma frase
Por meio da SPIFFE Workload API, o SPIRE emite dois formatos complementares de **SVID (SPIFFE Verifiable Identity Document)** baseados nos padrões do repositório `spiffe/spiffe`: o **X.509-SVID** (um certificado X.509 de curta duração contendo o `SPIFFE ID` na extensão Subject Alternative Name URI, acompanhado de sua chave privada e do *trust bundle* de autoridades certificadoras), utilizado para estabelecer conexões **mTLS (Mutual TLS)** ponta a ponta; e o **JWT-SVID** (um token JSON Web Token assinado criptograficamente contendo o `SPIFFE ID` no claim `sub` e a audiência alvo em `aud`), utilizado quando o tráfego atravessa proxies de camada 7 ou autentica em sistemas que consomem tokens Bearer/OIDC.

## Por que importa
Enquanto o **X.509-SVID** é ideal para criptografia e autenticação mútua direta no transporte TLS sem intermediários, certos balanceadores HTTP corporativos terminam o TLS no caminho ou serviços externos de nuvem/bancos de dados exigem um token **JWT** assinado para federação OIDC. Suportar ambos na mesma Workload API cobre qualquer topologia.

## Como funciona
Priorize **X.509-SVIDs** com mTLS sempre que possível (pois não são vulneráveis a ataques de replay de token interceptado) e utilize **JWT-SVIDs** com audiência (`aud`) estrita e tempo de expiração curto quando atravessar intermediários L7 ou autenticar via federação OIDC em provedores de nuvem.

## Exemplo
Um serviço em Go usa seu X.509-SVID para falar mTLS com o banco de dados interno e solicita um JWT-SVID com `aud: sts.amazonaws.com` à mesma SPIFFE Workload API para assumir uma role IAM temporária na AWS sem chaves estáticas.

## Limites e trade-offs
Nunca armazene a chave privada de um X.509-SVID em disco persistente nem reutilize um JWT-SVID sem validar rigorosamente o claim `aud` (audiência) no serviço verificador para impedir que um token enviado ao serviço B seja reencaminhado pelo serviço B para se passar pelo cliente no serviço C.

## Como verificar
Inspecione o certificado X.509-SVID emitido pelo SPIRE (`openssl x509 -text -noout`) e confirme que a extensão `X509v3 Subject Alternative Name` contém `URI:spiffe://<trust-domain>/<path>`.

## Conexões
- [[spiffe-spire-runtime-environment-and-workload-api]] — Veja também: SPIRE como ambiente de execução SPIFFE graduado na CNCF e exposição da SPIFFE Workload API.
- [[spiffe-spire-server-spire-agent-and-oidc-discovery-provider-images]] — Veja também: Componentes e imagens oficiais do SPIRE: spire-server, spire-agent e oidc-discovery-provider.

## Fontes
- [SPIRE GitHub — README.md (SPIFFE Runtime Environment, Workload API, SVIDs, Envoy SDS & Security Audits)](https://raw.githubusercontent.com/spiffe/spire/main/README.md) — README oficial do SPIRE (projeto graduado na CNCF sob Apache-2.0) detalhando implementação de produção do SPIFFE, SPIFFE Workload API, emissão de SPIFFE IDs e SVIDs (X.509 mTLS e JWT), imagens spire-server/spire-agent/oidc-discovery-provider, bibliotecas go-spiffe e java-spiffe, integração com Envoy SDS, framework de plugins e auditorias de segurança Cure53 (2021) e CNCF TAG-Security (2018 e 2020).; consultado em 2026-10-03.
- [SPIFFE & SPIRE Official Documentation — Quickstart Guides & Architecture](https://spiffe.io/spire/try/) — Portal oficial do SPIFFE e SPIRE com arquitetura de atestação de nó e workload, guias para Kubernetes/Linux/macOS e o livro gratuito Solving the Bottom Turtle.; consultado em 2026-10-03.
- [SPIRE — Official GitHub Repository](https://github.com/spiffe/spire) — Repositório oficial Apache-2.0 do SPIRE na CNCF.; consultado em 2026-10-03.
