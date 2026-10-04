---
id: software.seguranca.tranche15.001469
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/aircrack-ng/aircrack-ng/master/README.md", "https://www.aircrack-ng.org/doku.php?id=aircrack-ng"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Simulação de **Rogue Access Point / Evil Twin** com **`airbase-ng`** e Detecção de Ataques de Associação Automática em Auditorias Red Team

## Em uma frase
O que é um ataque de **Evil Twin / Rogue Access Point** simulado pela ferramenta **`airbase-ng`** da suíte Aircrack-ng durante um exercício autorizado de Red Team, e como ele explora dispositivos configurados para conectar automaticamente a redes abertas ou SSIDs conhecidos com o mesmo nome?

## Por que importa
O **`airbase-ng`** utiliza uma interface em Modo Monitor (`wlan0mon`) para atuar em software como um Access Point 802.11 multi-SSID (criando uma interface virtual `at0` TAP no Linux): ele pode anunciar um `ESSID` específico (`-e "Corp-Guest"`) ou responder a *Probe Requests* de clientes e testar se os dispositivos tentam se associar a um AP falso que imita o nome da rede legítima!

## Como funciona
Mais importante ainda: em redes **WPA2-Enterprise (`802.1X PEAP-MSCHAPv2`)** mal configuradas onde o cliente (notebook/celular) **não valida o Certificado X.509 do Servidor RADIUS (` Validate Server Certificate = Off`)**, um Evil Twin consegue fazer o cliente iniciar o túnel EAP com o AP falso!

## Exemplo
```bash
# Em ambiente de laboratorio isolado, simular um Access Point de teste com airbase-ng no canal 6 anunciando um SSID de homologacao
airbase-ng -e "Lab-Teste-Seguranca" -c 6 -v wlan0mon
```

## Limites e trade-offs
Como blindar 100% os notebooks e smartphones da sua empresa contra ataques de **Evil Twin** em redes **WPA2/WPA3-Enterprise (`802.1X`)**? **(1) Migre de `PEAP-MSCHAPv2` (baseado em senha) para `EAP-TLS` (baseado em Certificados X.509 de Máquina/Usuário emitidos pela Dogtag PKI do FreeIPA, Step-CA ou AD CS e guardados no TPM 2.0 / YubiKey PIV!)**; e **(2) Nos perfis de rede gerenciados por MDM/GPO/NetworkManager, fixe obrigatoriamente a CA Raiz interna (`ca_cert`) e o `domain_suffix_match = radius.empresa.br`**, proibindo o usuário de clicar em *"Confiar neste certificado desconhecido"*!

## Como verificar
Combine essa blindagem nos endpoints com sensores **WIDS (Kismet)** ou proteção de Rogue AP dos controladores Wi-Fi corporativos para alertar imediatamente se surgir qualquer BSSID desconhecido anunciando os SSIDs da empresa.

## Conexões
- [[aircrack-analise-grafos-airgraph-ng-relacoes-capr-cpg-clientes-probes]] — Veja também: Mapeamento Visual de Relações Sem Fio com **`airgraph-ng`**: Grafos **`CAPR` (*Client to AP Relationship*)** e **`CPG` (*Common Probe Graph*)** a partir do CSV do `airodump-ng`.
- [[aircrack-evolucao-wpa3-sae-dragonfly-wpa2-enterprise-8021x-mitigacao]] — Veja também: Do WEP (`PTW`/`KoreK`) e WPA2-PSK ao **WPA3-SAE (*Simultaneous Authentication of Equals* / Dragonfly)** e **OWE**: Por que o WPA3 Elimina o Cracking Offline de Handshakes?.
- [[aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection]] — Referência cruzada direta com aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection.
- [[kismet-deteccao-intrusao-wids-alertas-deauth-flood-evil-twin-rogue-ap]] — Referência cruzada direta com kismet-deteccao-intrusao-wids-alertas-deauth-flood-evil-twin-rogue-ap.
- [[freeipa-pki-dogtag-certmonger-auto-renovacao-mtls-subca]] — Referência cruzada direta com freeipa-pki-dogtag-certmonger-auto-renovacao-mtls-subca.

## Fontes
- [Aircrack-ng Official GitHub Repository (`aircrack-ng/aircrack-ng`)](https://raw.githubusercontent.com/aircrack-ng/aircrack-ng/master/README.md) — repositório oficial da suíte Aircrack-ng cobrindo ferramentas de monitoramento, captura, injeção de quadros 802.11, teste de chaves WPA/WPA2 e descriptografia `airdecap-ng`; consultado em 2026-10-03.
- [Aircrack-ng Official Technical Documentation (`aircrack-ng.org`)](https://www.aircrack-ng.org/doku.php?id=aircrack-ng) — documentação técnica oficial do `aircrack-ng` detalhando ataques de dicionário WPA/WPA2-PSK (`PBKDF2-HMAC-SHA1`), bancos pré-computados `airolib-ng` e flags operacionais; consultado em 2026-10-03.
