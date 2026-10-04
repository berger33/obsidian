---
id: software.seguranca.tranche09.000840
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

# Pipeline de Descoberta Recursiva por Certificados: **`subfinder` -> `dnsx` -> `naabu` -> `tlsx -dns` -> `httpx` -> `nuclei`**

## Em uma frase
Combinar o **`tlsx`** dentro do pipeline ProjectDiscovery cria um **loop de retroalimentação de descoberta de ativos**: primeiro você descobre subdomínios passivos (`subfinder`), resolve os IPs (`dnsx`), descobre as portas abertas (`naabu`) e então usa o **`tlsx -san -cn -ro`** sobre esses hosts/portas para **descobrir novos subdomínios internos e domínios irmãos que só existiam dentro dos certificados X.509**!

## Por que importa
Além do uso em linha de comando, conforme documentado no `README.md` (`Using tlsx as library`), o pacote Go **`github.com/projectdiscovery/tlsx/pkg/tlsx`** pode ser importado diretamente em microsserviços de segurança internos em Go para validar certificados e coletar fingerprints JARM/JA3 programaticamente.

## Como funciona
Quando integrado ao dashboard `PDCP` (`-pd`) ou exportado em JSONL (`-json`), o `tlsx` mantém o inventário criptográfico de toda a organização atualizado.

## Exemplo
```bash
# Extrair novos subdominios ocultos nos certificados TLS das portas abertas pelo Naabu e sondar tudo com o httpx
naabu -l /cases/easm/resolved_subdomains.txt -top-ports 1000 -exclude-cdn -silent \
  | tlsx -san -cn -silent -resp-only \
  | sort -u \
  | dnsx -silent \
  | httpx -silent -title -status-code -tech-detect -o /cases/easm/expanded_web_surface.txt
```

## Limites e trade-offs
Observe como o passo `tlsx -san -cn -silent -resp-only | sort -u | dnsx -silent` atua como um multiplicador de superfície de ataque: um único servidor que hospede 30 microsserviços no mesmo certificado multi-SAN revela todos os 30 FQDNs de uma só vez!

## Como verificar
Agende esse pipeline semanalmente e compare os novos nomes descobertos com o histórico do `oam_track` (Amass).

## Conexões
- [[tlsx-varredura-multi-porta-starttls-proxies-socks5-concorrencia]] — Veja também: `tlsx`: Varredura TLS em **Portas Não-Padrão (`-p 443,8443,9443,6443,2379,636`)**, Controle de Concorrência (`-c`, `-delay`) e Proxy **`-proxy`**.
- [[tlsx-arquitetura-coletor-tls-modos-ctls-ztls-openssl-auto]] — Referência cruzada direta com tlsx-arquitetura-coletor-tls-modos-ctls-ztls-openssl-auto.
- [[tlsx-descoberta-subdominios-certificados-san-cn-dns-cidr-asn]] — Referência cruzada direta com tlsx-descoberta-subdominios-certificados-san-cn-dns-cidr-asn.
- [[naabu-integracao-pipeline-subfinder-dnsx-naabu-httpx-nuclei]] — Referência cruzada direta com naabu-integracao-pipeline-subfinder-dnsx-naabu-httpx-nuclei.

## Fontes
- [ProjectDiscovery tlsx Official GitHub — Fast and Configurable TLS Grabber Focused on TLS Data Collection](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/README.md) — repositório oficial do ProjectDiscovery tlsx cobrindo os 4 motores TLS, extração SAN/CN, auditoria de certificados/cifras e hashes JA3/JARM; consultado em 2026-10-03.
- [ProjectDiscovery tlsx Official Documentation — Scan Modes & Certificate Analysis](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/go.mod) — documentação oficial do tlsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/tlsx](https://docs.projectdiscovery.io/tools/tlsx/overview) — referência técnica do pacote Go `projectdiscovery/tlsx`; consultado em 2026-10-03.
