---
id: software.seguranca.tranche04.000307
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

# OpenZiti: Criptografia Ponta a Ponta (`libsodium` Curve25519 / ChaCha20-Poly1305) Acima do mTLS

## Em uma frase
Além do mTLS obrigatório em cada salto entre clientes e *Edge Routers*, o OpenZiti oferece criptografia ponta a ponta (*end-to-end encryption*) nativa baseada em `libsodium` entre a identidade de origem (`Dial`) e a identidade hospedeira (`Bind`).

## Por que importa
Mesmo que um *Edge Router* ou *Fabric Router* intermediário em nuvem pública seja comprometido ou inspecionado na memória, o atacante não consegue decifrar nem adulterar o payload da aplicação.

## Como funciona
Quando um serviço exige `--encryption ON`, o SDK/tunneler de origem e o SDK/tunneler de destino realizam troca de chaves efêmeras (`crypto_kx` sobre Curve25519) e cifram o fluxo de dados com AEAD (`crypto_secretstream_xchacha20poly1305`) antes de injetá-lo no túnel mTLS da malha.

## Exemplo
```bash
# Auditar todos os serviços OpenZiti para garantir que encryptionRequired está ativado
ziti edge list services -j \
  | jq -r '.data[] | select(.encryptionRequired == false) | .name'

# Forçar criptografia ponta a ponta obrigatória em um serviço existente
ziti edge update service "corp-postgres" --encryption ON
```

## Limites e trade-offs
Se um serviço for criado com `--encryption OFF`, o tráfego ainda estará cifrado via mTLS entre os saltos dos roteadores, mas ficará em texto claro na memória transitória dos roteadores da malha.

## Como verificar
Execute a consulta JSON `ziti edge list services -j | jq '.data[] | {name, encryptionRequired}'` e confirme que todos os serviços críticos exibem `"encryptionRequired": true`.

## Conexões
- [[ziti-tunnelers-ziti-edge-tunnel-intercept-host-tproxy-dns]] — Veja também: OpenZiti: Tunnelers (`ziti-edge-tunnel`) com Interceptação DNS/TPROXY (`intercept.v1`) e Hosting (`host.v1`).
- [[ziti-posture-checks-mfa-os-process-mac-domain-avaliacao-continua]] — Veja também: OpenZiti: Posture Checks Contínuos (OS, Processos, MAC, Domínio e MFA TOTP).
- [[ziti-arquitetura-openziti-malha-zero-trust-controller-fabric-edge]] — Referência cruzada direta com ziti-arquitetura-openziti-malha-zero-trust-controller-fabric-edge.
- [[ziti-sdks-application-embedded-zero-trust-go-c-python-jvm]] — Referência cruzada direta com ziti-sdks-application-embedded-zero-trust-go-c-python-jvm.

## Fontes
- [OpenZiti GitHub — README.md (Zero Trust Overlay Network, Dark Services and Routers, End-to-End Encryption, SDKs & Tunnelers)](https://raw.githubusercontent.com/openziti/ziti/release-next/README.md) — README oficial do openziti/ziti apresentando a arquitetura do Controller, Fabric Mesh, Edge Components e serviços dark; consultado em 2026-10-03.
- [OpenZiti Official Documentation — Introduction & Core Concepts (Controllers, Routers, Edge Clients, Services, Identities & Policies)](https://netfoundry.io/docs/openziti/intro/) — Documentação oficial de introdução ao OpenZiti detalhando segmentação por aplicação, mTLS X.509 e criptografia ponta a ponta via libsodium; consultado em 2026-10-03.
- [OpenZiti — Official GitHub Changelog & Repository](https://github.com/openziti/ziti/blob/release-next/CHANGELOG.md) — Repositório oficial Apache-2.0 do OpenZiti; consultado em 2026-10-03.
