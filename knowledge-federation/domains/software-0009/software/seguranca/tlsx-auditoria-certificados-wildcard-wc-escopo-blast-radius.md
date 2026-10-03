---
id: software.seguranca.tranche09.000838
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

# `tlsx` **`-wc` (`-wildcard-cert`)**: Mapeamento de **Certificados Wildcard (`*.dominio`)** e Redução do *Blast Radius* de Chaves Privadas

## Em uma frase
Embora certificados **Wildcard (`*.exemplo.com.br`)** sejam convenientes para operações, compartilhar o mesmo certificado (e portanto a **mesma chave privada TLS**!) entre dezenas de servidores diferentes — misturando o blog de marketing em WordPress com a API financeira crítica no mesmo `*.exemplo.com.br` — cria um **Raio de Explosão (*Blast Radius*)** perigoso.

## Por que importa
Se um único servidor menos seguro que possui a chave privada de `*.exemplo.com.br` sofrer leitura de arquivos (LFI/SSRF/comprometimento), o atacante obtém a chave privada capaz de personificar ou decifrar tráfego passivo não-PFS de **todos os outros subdomínios sob `*.exemplo.com.br`**!

## Como funciona
A flag **`-wc` / `-wildcard-cert`** do `tlsx` filtra e lista todos os hosts da organização que utilizam certificados wildcard, permitindo cruzar pelo **`-hash sha256`** / **`-serial`** exatamente quais servidores compartilham o mesmo arquivo de certificado/chave privada!

## Exemplo
```bash
# Mapear todos os ativos que utilizam certificados Wildcard (-wc) agrupando pelo numero de serie (-se) e hash SHA-256
tlsx -l /cases/easm/live_web_assets.txt \
  -wildcard-cert -cn -san -serial -hash sha256 \
  -json -o /cases/easm/wildcard_blast_radius.jsonl
```

## Limites e trade-offs
Ao analisar o arquivo `wildcard_blast_radius.jsonl` com `jq -r '[.host, .serial, .subject_cn] | @tsv'`, identifique se servidores de terceiros ou ambientes de *staging/dev* estão compartilhando o mesmo `serial` do certificado wildcard de produção.

## Como verificar
Recomende substituir certificados wildcard amplos por certificados individuais de curta duração automatizados por serviço via **Certbot / cert-manager ACME**.

## Conexões
- [[tlsx-exportacao-cadeia-pem-certificate-tls-chain-client-server-hello]] — Veja também: `tlsx`: Exportação Completa da **Cadeia de Certificados em PEM (`-cert`, `-tls-chain`)** e Transcrição **`-client-hello` / `-server-hello`**.
- [[tlsx-varredura-multi-porta-starttls-proxies-socks5-concorrencia]] — Veja também: `tlsx`: Varredura TLS em **Portas Não-Padrão (`-p 443,8443,9443,6443,2379,636`)**, Controle de Concorrência (`-c`, `-delay`) e Proxy **`-proxy`**.
- [[tlsx-arquitetura-coletor-tls-modos-ctls-ztls-openssl-auto]] — Referência cruzada direta com tlsx-arquitetura-coletor-tls-modos-ctls-ztls-openssl-auto.
- [[tlsx-fingerprinting-ativo-jarm-ja3-hashes-certificados-shodan]] — Referência cruzada direta com tlsx-fingerprinting-ativo-jarm-ja3-hashes-certificados-shodan.

## Fontes
- [ProjectDiscovery tlsx Official GitHub — Fast and Configurable TLS Grabber Focused on TLS Data Collection](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/README.md) — repositório oficial do ProjectDiscovery tlsx cobrindo os 4 motores TLS, extração SAN/CN, auditoria de certificados/cifras e hashes JA3/JARM; consultado em 2026-10-03.
- [ProjectDiscovery tlsx Official Documentation — Scan Modes & Certificate Analysis](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/go.mod) — documentação oficial do tlsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/tlsx](https://docs.projectdiscovery.io/tools/tlsx/overview) — referência técnica do pacote Go `projectdiscovery/tlsx`; consultado em 2026-10-03.
