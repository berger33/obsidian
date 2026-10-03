---
id: software.seguranca.tranche09.000835
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

# `tlsx`: Enumeração de **Versões TLS Suportadas (`-ve` / `-version-enum`)** e Auditoria de **Cifras Fracas/Inseguras (`-ce` / `-cipher-enum`, `-ct`)**

## Em uma frase
Conectar uma única vez em um servidor TLS mostra apenas a versão e a cifra preferida daquele handshake (`TLS 1.3` + `TLS_AES_128_GCM_SHA256`), mas **não** revela se o mesmo servidor ainda aceita silenciosamente conexões **`TLS 1.0`**, **`TLS 1.1`** ou cifras fracas sem *Forward Secrecy* (`TLS_RSA_WITH_3DES_EDE_CBC_SHA`) quando solicitado por um cliente antigo ou atacante!

## Por que importa
Para auditar a matriz completa de protocolos e cifras aceitos por milhares de endpoints em minutos, o `tlsx` fornece as flags **`-ve` (`-version-enum`)** e **`-ce` (`-cipher-enum`)**!

## Como funciona
Combinando **`-ce`** com o filtro **`-ct` (`-cipher-type`, valores: `all`, `secure`, `insecure`, `weak`)** e **`-cec` (`-cipher-concurrency`)**, você pode instruir o `tlsx` a testar especificamente se algum servidor da organização aceita cifras classificadas como **`weak` ou `insecure`**!

## Exemplo
```bash
# Enumerar todas as versoes de TLS suportadas (-ve) e testar especificamente cifras fracas/inseguras (-ce -ct weak,insecure)
tlsx -l /cases/easm/live_web_assets.txt \
  -version-enum \
  -cipher-enum -cipher-type weak,insecure \
  -sm auto \
  -json -o /cases/easm/weak_tls_audit.jsonl
```

## Limites e trade-offs
Por que `-ct weak,insecure` é muito mais rápido em CI/CD e monitoramento contínuo do que `-ct all`? Porque em vez de testar dezenas de cifras modernas seguras que você já sabe que são permitidas, ele sonda apenas o subconjunto de cifras obsoletas/inseguras que violam a política de conformidade (PCI-DSS v4.0 / BACEN)!

## Como verificar
Filtre no `weak_tls_audit.jsonl` qualquer host cuja lista `.version_enum` contenha `"tls10"` ou `"tls11"`, ou que apresente cifras em `.cipher_enum`.

## Conexões
- [[tlsx-fingerprinting-ativo-jarm-ja3-hashes-certificados-shodan]] — Veja também: `tlsx`: Fingerprinting Criptográfico **`-jarm`**, **`-ja3`**, Serial (`-se`) e Hashes de Certificado (**`-hash md5,sha1,sha256`**) para Threat Hunting.
- [[tlsx-customizacao-sni-random-sni-rev-ptr-sni-virtual-hosts]] — Veja também: `tlsx`: Manipulação Avançada de **TLS SNI (`-sni`, `-random-sni`, `-rev-ptr-sni`)** para Descoberta de *Virtual Hosts* e Bypass de Roteamento.
- [[tlsx-arquitetura-coletor-tls-modos-ctls-ztls-openssl-auto]] — Referência cruzada direta com tlsx-arquitetura-coletor-tls-modos-ctls-ztls-openssl-auto.

## Fontes
- [ProjectDiscovery tlsx Official GitHub — Fast and Configurable TLS Grabber Focused on TLS Data Collection](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/README.md) — repositório oficial do ProjectDiscovery tlsx cobrindo os 4 motores TLS, extração SAN/CN, auditoria de certificados/cifras e hashes JA3/JARM; consultado em 2026-10-03.
- [ProjectDiscovery tlsx Official Documentation — Scan Modes & Certificate Analysis](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/go.mod) — documentação oficial do tlsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/tlsx](https://docs.projectdiscovery.io/tools/tlsx/overview) — referência técnica do pacote Go `projectdiscovery/tlsx`; consultado em 2026-10-03.
