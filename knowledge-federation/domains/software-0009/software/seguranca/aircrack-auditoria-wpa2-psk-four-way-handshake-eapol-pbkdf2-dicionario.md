---
id: software.seguranca.tranche15.001465
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

# Anatomia do **4-Way Handshake EAPOL** no WPA/WPA2-PSK e Auditoria com **`aircrack-ng -w`**: `PMK`, `PTK`, `ANonce`, `SNonce`, `MIC` e Pares de Mensagens (`2+3` ou `3+4`)

## Em uma frase
O que realmente trafega nos **4 quadros EAPOL (`Extensible Authentication Protocol over LAN`)** quando um dispositivo conecta a um Wi-Fi **WPA2-PSK**, por que a senha (`Passphrase`) nunca viaja pelo ar, e **por que a documentação oficial do `aircrack-ng` explica que bastam apenas 2 dos 4 pacotes (`mensagens 2 e 3` ou `mensagens 3 e 4`) para auditar a senha**?

## Por que importa
Veja a matemática do WPA2-PSK: primeiro, ambos os lados derivam a **PMK (*Pairwise Master Key*, 256 bits)** aplicando **`PBKDF2-HMAC-SHA1(Passphrase, ESSID, 4096 iterações)`**. Como a `PMK` é sempre a mesma para a mesma senha, ela não é usada diretamente para cifrar pacotes; em vez disso, o AP e o Cliente trocam o **4-Way Handshake** para derivar uma chave efêmera de sessão chamada **PTK (*Pairwise Transient Key*)** a partir de `PRF(PMK, "Pairwise key expansion", Min/Max(AA, SPA) || Min/Max(ANonce, SNonce))`!

## Como funciona
Por que o `aircrack-ng` precisa apenas dos pacotes EAPOL **`(2 e 3)`** ou **`(3 e 4)`**? Porque para testar uma senha do dicionário (`-w wordlist.txt`), o `aircrack-ng` só precisa conhecer: **(1) O `ESSID`**, **(2) Os dois MACs (`AA` do AP e `SPA` do Cliente)**, **(3) Os dois números aleatórios (`ANonce` enviado pelo AP nas mensagens 1 e 3, e `SNonce` enviado pelo Cliente na mensagem 2)** e **(4) O código de integridade `EAPOL MIC` assinado com a `KCK` da `PTK`**!

## Exemplo
```bash
# Auditar a forca da senha WPA2-PSK de um arquivo .cap contendo o 4-Way Handshake EAPOL usando dicionario e filtrando pelo BSSID (-b)
aircrack-ng -w ./dicionario_auditoria.txt -b AA:BB:CC:DD:EE:FF ./auditoria_corp-01.cap
```

## Limites e trade-offs
E se você quiser combinar o gerador de regras de mutação (**Mangling Rules / `--single-seed`**) do **John the Ripper** com o motor SIMD AVX2/AVX-512 do **`aircrack-ng`** sem precisar gravar um dicionário gigante no disco? Basta conectar os dois por um pipe Unix usando **`-w -`** (stdin): **`john --wordlist=base.txt --rules=best64 --stdout | aircrack-ng -e "Corp-WiFi" -w - ./auditoria_corp-01.cap`**!

## Como verificar
Para extrair e limpar apenas os pacotes do 4-Way Handshake de um arquivo `.pcap` gigante de vários gigabytes (conforme recomendado na documentação do `aircrack-ng`), use a ferramenta **`wpaclean ./handshake_limpo.cap ./captura_gigante.cap`** incluída na suíte!

## Conexões
- [[aircrack-injecao-pacotes-aireplay-ng-teste-driver-deauth-80211w-pmf]] — Veja também: Injeção de Quadros e Teste de Resiliência **IEEE 802.11w (`PMF` — *Protected Management Frames*)** com **`aireplay-ng`**: `--test` (`-9`) e `--deauth` (`-0`).
- [[aircrack-precomputacao-pmk-airolib-ng-sqlite-rainbow-tables-essid]] — Veja também: Pré-Computação de **Pairwise Master Keys (`PMK`)** com **`airolib-ng`** e `aircrack-ng -r`: Acelerando Auditorias em `1.000x` sobre SSIDs Padronizados.
- [[aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection]] — Referência cruzada direta com aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection.
- [[john-modo-wordlist-regras-mangling-rules-best64-korelogic-custom]] — Referência cruzada direta com john-modo-wordlist-regras-mangling-rules-best64-korelogic-custom.

## Fontes
- [Aircrack-ng Official GitHub Repository (`aircrack-ng/aircrack-ng`)](https://raw.githubusercontent.com/aircrack-ng/aircrack-ng/master/README.md) — repositório oficial da suíte Aircrack-ng cobrindo ferramentas de monitoramento, captura, injeção de quadros 802.11, teste de chaves WPA/WPA2 e descriptografia `airdecap-ng`; consultado em 2026-10-03.
- [Aircrack-ng Official Technical Documentation (`aircrack-ng.org`)](https://www.aircrack-ng.org/doku.php?id=aircrack-ng) — documentação técnica oficial do `aircrack-ng` detalhando ataques de dicionário WPA/WPA2-PSK (`PBKDF2-HMAC-SHA1`), bancos pré-computados `airolib-ng` e flags operacionais; consultado em 2026-10-03.
