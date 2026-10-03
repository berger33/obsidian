---
id: software.seguranca.tranche09.000832
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/projectdiscovery/tlsx/main/README.md", "https://raw.githubusercontent.com/projectdiscovery/tlsx/main/go.mod", "https://docs.projectdiscovery.io/tools/tlsx/overview"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `tlsx`: Descoberta Ativa de Subdomínios e Ativos via **Campos `SAN` (`-san`) e `CN` (`-cn`)** sobre Blocos **CIDR e ASNs** e Modo **`-pre-handshake` (`-ps`)**

## Em uma frase
Quando você varre um bloco de endereços IP (**CIDR**, ex.: `198.51.100.0/24`) ou um **ASN (`AS1449`)** na porta `443`, cada servidor HTTPS apresenta na fase inicial do handshake TLS o seu certificado X.509 contendo o **Subject Common Name (`-cn`)** e a lista de **Subject Alternative Names (`-san`)** — que frequentemente lista dezenas de subdomínios internos e domínios irmãos da empresa!

## Por que importa
No `tlsx`, combinar **`-san -cn`** (ou a flag **`-dns`**, que extrai exclusivamente os nomes de host únicos encontrados dentro dos certificados SSL/TLS!) com **`-ro` (`-resp-only`)** transforma qualquer faixa de IPs em uma fonte riquíssima de novos subdomínios!

## Como funciona
Ainda mais impressionante para varreduras em larga escala é a flag **`-ps` / `-pre-handshake`** (disponível com `ztls`): no TLS 1.2, o servidor envia a mensagem `Certificate` **antes** da troca de chaves final e do `Finished`; com `-ps`, o `tlsx` **lê o certificado X.509 e encerra a conexão imediatamente antes de completar o handshake criptográfico**, multiplicando a velocidade e reduzindo o uso de CPU!

## Exemplo
```bash
# Varrer um bloco CIDR extraindo todos os subdominios unicos presentes nos campos SAN e CN dos certificados X.509 (-dns -ro)
tlsx -u 10.20.0.0/16 \
  -p 443,8443 \
  -san -cn -dns -resp-only \
  -pre-handshake \
  -c 300 \
  -o /cases/easm/subdomains_from_tls_certs.txt
```

## Limites e trade-offs
Para extrair também o nome legal da empresa proprietária do certificado (útil para atribuir ativos durante o reconhecimento horizontal `amass intel`), adicione a flag **`-so` (`-subject-org`)**!

## Como verificar
Encadeie a saída de `tlsx -san -cn -ro` diretamente para `grep -E '\.exemplo\.com\.br$' | sort -u | dnsx -silent` para validar os novos subdomínios descobertos nos certificados.

## Conexões
- [[tlsx-arquitetura-coletor-tls-modos-ctls-ztls-openssl-auto]] — Veja também: ProjectDiscovery **`tlsx`**: Arquitetura do Coletor e Analisador TLS e os 4 Motores de Conexão (**`ctls`**, **`ztls`**, **`openssl`** e **`auto`**).
- [[tlsx-deteccao-misconfigurations-expired-self-signed-mismatched-revoked]] — Veja também: `tlsx`: Auditoria Contínua de **Misconfigurations de Certificados X.509** (`-ex` Expirado, `-ss` Auto-Assinado, `-mm` Mismatched, `-re` Revogado e `-un` Untrusted).
- [[amass-descoberta-intel-asn-cidr-reverse-whois-organizacoes]] — Referência cruzada direta com amass-descoberta-intel-asn-cidr-reverse-whois-organizacoes.
- [[dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros]] — Referência cruzada direta com dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros.

## Fontes
- [ProjectDiscovery tlsx Official GitHub — Fast and Configurable TLS Grabber Focused on TLS Data Collection](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/README.md) — repositório oficial do ProjectDiscovery tlsx cobrindo os 4 motores TLS, extração SAN/CN, auditoria de certificados/cifras e hashes JA3/JARM; consultado em 2026-10-03.
- [ProjectDiscovery tlsx Official Documentation — Scan Modes & Certificate Analysis](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/go.mod) — documentação oficial do tlsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/tlsx](https://docs.projectdiscovery.io/tools/tlsx/overview) — referência técnica do pacote Go `projectdiscovery/tlsx`; consultado em 2026-10-03.
