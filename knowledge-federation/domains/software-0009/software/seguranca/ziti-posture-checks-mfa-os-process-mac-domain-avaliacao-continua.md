---
id: software.seguranca.tranche04.000308
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/openziti/ziti/release-next/README.md", "https://netfoundry.io/docs/openziti/intro/", "https://github.com/openziti/ziti/blob/release-next/CHANGELOG.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OpenZiti: Posture Checks Contínuos (OS, Processos, MAC, Domínio e MFA TOTP)

## Em uma frase
*Posture Checks* no OpenZiti avaliam continuamente atributos de estado do dispositivo cliente (versão mínima do SO, hash/assinatura de processos EDR em execução, domínio Windows, MAC e MFA TOTP) antes e durante as sessões de rede.

## Por que importa
Evita que um endpoint cujo certificado seja válido, mas cujo agente de EDR tenha sido encerrado ou cuja sessão MFA tenha expirado, mantenha conexões abertas com serviços internos sensíveis.

## Como funciona
As checagens de postura são criadas no Controller (`ziti edge create posture-check ...`) e vinculadas às `service-policies` via `--posture-check-roles`. O cliente envia telemetria periódica de postura; se uma checagem falhar no meio de uma transferência TCP ativa, o OpenZiti encerra imediatamente os circuitos abertos daquela identidade.

## Exemplo
```bash
# Exigir Linux kernel >= 6.1.0 e MFA TOTP válido com timeout de inatividade de 15 minutos
ziti edge create posture-check os "linux-min-kernel" \
  --os "Linux:6.1.0" -a "prod-posture"

ziti edge create posture-check mfa "totp-15m" \
  --timeout 900 --prompt-on-wake --prompt-on-unlock -a "prod-posture"

ziti edge update service-policy "sre-dial-prod-k8s" \
  --posture-check-roles "#prod-posture"
```

## Limites e trade-offs
Verificações de processos por hash SHA-512 exigem atualização da política sempre que o agente de segurança (ex.: CrowdStrike/Falco) sofrer atualização automática nos endpoints corporativos.

## Como verificar
Execute `ziti edge policy-advisor services "corp-postgres" -q` ou inspecione as falhas de postura da identidade na API REST para confirmar que sessões sem MFA ou fora da versão do SO são bloqueadas.

## Conexões
- [[ziti-criptografia-ponta-a-ponta-libsodium-kx-chacha20-poly1305]] — Veja também: OpenZiti: Criptografia Ponta a Ponta (`libsodium` Curve25519 / ChaCha20-Poly1305) Acima do mTLS.
- [[ziti-smart-routing-fabric-mesh-terminators-load-balancing-ha]] — Veja também: OpenZiti: Smart Routing na Fabric Mesh, Terminators, Custos Dinâmicos e Alta Disponibilidade.
- [[ziti-identities-enrollment-jwt-ott-certificados-x509-mutuos]] — Referência cruzada direta com ziti-identities-enrollment-jwt-ott-certificados-x509-mutuos.
- [[ziti-politicas-service-policies-edge-router-policies-bind-dial]] — Referência cruzada direta com ziti-politicas-service-policies-edge-router-policies-bind-dial.
- [[ziti-arquitetura-openziti-malha-zero-trust-controller-fabric-edge]] — Referência cruzada direta com ziti-arquitetura-openziti-malha-zero-trust-controller-fabric-edge.

## Fontes
- [OpenZiti GitHub — README.md (Zero Trust Overlay Network, Dark Services and Routers, End-to-End Encryption, SDKs & Tunnelers)](https://raw.githubusercontent.com/openziti/ziti/release-next/README.md) — README oficial do openziti/ziti apresentando a arquitetura do Controller, Fabric Mesh, Edge Components e serviços dark; consultado em 2026-10-03.
- [OpenZiti Official Documentation — Introduction & Core Concepts (Controllers, Routers, Edge Clients, Services, Identities & Policies)](https://netfoundry.io/docs/openziti/intro/) — Documentação oficial de introdução ao OpenZiti detalhando segmentação por aplicação, mTLS X.509 e criptografia ponta a ponta via libsodium; consultado em 2026-10-03.
- [OpenZiti — Official GitHub Changelog & Repository](https://github.com/openziti/ziti/blob/release-next/CHANGELOG.md) — Repositório oficial Apache-2.0 do OpenZiti; consultado em 2026-10-03.
